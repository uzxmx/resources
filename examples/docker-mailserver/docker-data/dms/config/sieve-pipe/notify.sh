#!/bin/sh
# 由 Sieve pipe 调用。参数:$1=发件人  $2=未知主题  $3=收件人
# 调用 notify 接口(企业微信告警)。

# ===== 按实际情况填写 =====
APP_BASE_URL="https://your-app-host"
SUBSCRIBER_ID="xxx"
SUBSCRIBER_TOKEN="xxx"
# TOUSER="zhangsan"                        # 可选:企业微信指定接收人
# =========================

sender="$1"
subject="$2"
receiver="$3"

# pipe 会把整封邮件送到 stdin,这里不需要,丢弃以避免 SIGPIPE
cat >/dev/null 2>&1

message="未知主题邮件已转发
收件人:${receiver}
发件人:${sender}
未知主题:${subject}"

curl -s -m 10 -X POST "${APP_BASE_URL}/notify" \
  -H "X-Subscriber-Id: ${SUBSCRIBER_ID}" \
  -H "X-Subscriber-Token: ${SUBSCRIBER_TOKEN}" \
  --data-urlencode "message=${message}" \
  ${TOUSER:+--data-urlencode "touser=${TOUSER}"} \
  >/dev/null 2>&1

exit 0
