#!/bin/bash
# docker-mailserver 启动时执行。定义慢速 transport,给发往 QQ/163 的邮件限速。

# 新建 master.cf 服务:slow(基于 smtp 投递代理)
postconf -Me "slow/unix=slow unix - - n - - smtp"

# 该服务的限速参数
postconf -P "slow/unix/syslog_name=postfix-slow"
postconf -P "slow/unix/smtp_destination_rate_delay=120s"
postconf -P "slow/unix/smtp_destination_concurrency_limit=1"

# --- 账号重建改为原子替换 ---
# 原因：docker-mailserver 12.1.0 的 _create_accounts 先清空 /etc/dovecot/userdb 和
# /etc/postfix/vmailbox 再逐行追加，重建期间（账号多时几十秒）已有用户会认证失败、
# 来信可能被 550 退回；且以 root mkdir 用户目录、最后才 chown，新用户登录会 Permission denied。
# 做法：先写 *.new 再 mv 原子替换；用户目录直接以 5000:5000 创建。
# 防护：只在 accounts.sh 与 12.1.0 原版完全一致时打补丁，否则跳过并告警（升级镜像后需重新评估）。
DMS_ACCOUNTS_SH=/usr/local/bin/helpers/accounts.sh
DMS_ACCOUNTS_SH_SHA256=a75848a1b932068d53768eb485f7fbd008616fc82e8249d12622224b60b0a8e2
if grep -q '__dms_orig_create_accounts' "${DMS_ACCOUNTS_SH}"; then
  echo 'user-patches: accounts.sh 已打过原子替换补丁，跳过'
elif [[ "$(sha256sum "${DMS_ACCOUNTS_SH}" | cut -d' ' -f1)" != "${DMS_ACCOUNTS_SH_SHA256}" ]]; then
  echo 'user-patches: WARNING accounts.sh 与 12.1.0 原版不一致（镜像已升级？），未打原子替换补丁' >&2
else
  sed -i \
    -e 's#^DOVECOT_USERDB_FILE=/etc/dovecot/userdb$#DOVECOT_USERDB_FILE=/etc/dovecot/userdb.new#' \
    -e 's#/etc/postfix/vmailbox#/etc/postfix/vmailbox.new#g' \
    -e 's#^\([[:space:]]*\)mkdir -p "/var/mail/${DOMAIN}/${USER}"$#\1[[ -d "/var/mail/${DOMAIN}/${USER}" ]] || install -d -o 5000 -g 5000 "/var/mail/${DOMAIN}/${USER}"#' \
    "${DMS_ACCOUNTS_SH}"
  cat >>"${DMS_ACCOUNTS_SH}" <<'PATCH'

# user-patches: 先写 *.new 再原子 rename，避免重建期间 userdb/vmailbox 为空
eval "$(declare -f _create_accounts | sed '1s/^_create_accounts/__dms_orig_create_accounts/')"
function _create_accounts
{
  __dms_orig_create_accounts "$@"
  local RC=$?
  mv -f /etc/dovecot/userdb.new /etc/dovecot/userdb
  mv -f /etc/postfix/vmailbox.new /etc/postfix/vmailbox
  return ${RC}
}
PATCH
  if bash -n "${DMS_ACCOUNTS_SH}"; then
    echo 'user-patches: accounts.sh 原子替换补丁已应用'
  else
    echo 'user-patches: ERROR 补丁后 accounts.sh 语法错误' >&2
  fi
fi

# --- mail.log 保留一年 ---
# _setup_logrotate 写死 rotate 4（weekly 下只有约 1 个月），这里改成 52 份 ≈ 1 年。
# mail.info/warn/err 由 rsyslog 的 logrotate 配置管理，内容是 mail.log 的子集，保持默认 4 份。
sed -i "s/^\([[:space:]]*\)rotate [0-9]\+$/\1rotate 52/" /etc/logrotate.d/maillog
echo "user-patches: mail.log logrotate 保留份数设为 52"
