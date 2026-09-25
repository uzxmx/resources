require ["copy", "envelope", "variables", "enotify", "vnd.dovecot.pipe"];

# 只处理发往 example.com 的邮件
if envelope :domain :is "to" "example.com" {

    # 列表一:主题命中则「不转发」,仅正常投递到信箱;否则转发到 QQ / 163
    if not header :contains "subject" [
        "case-insensitive subject 1",
        "case-insensitive subject 2",
        "test subject 3"
    ] {
        # 转发一份到 QQ 和 163,同时保留原件
        redirect :copy "test@qq.com";
        redirect :copy "test@163.com";

        # 取出发件人和主题(已解码),供下面两个通知分支共用
        if header :matches "subject" "*" { set "subj" "${1}"; }
        if header :matches "from"    "*" { set "sender" "${1}"; }
        if envelope :matches "to"    "*" { set "receiver" "${1}"; }

        # 列表二:已知正常主题,命中则不发邮件通知;其余未知主题邮件通知 admin
        if not header :contains "subject" [
          "case-insensitive subject 4",
          "case-insensitive subject 5",
          "test subject 6"
        ] {
            # :message 作为通知邮件标题(固定);正文通过 mailto 的 ?body= 传入
            # ?body= 内容(URL 编码后)解码为:
            #   发件人:${sender}
            #   未知主题:${subj}
            notify :importance "2"
                   :message "未知主题邮件已转发"
                   "mailto:admin@163.com?body=%E5%8F%91%E4%BB%B6%E4%BA%BA%EF%BC%9A${sender}%0A%E6%9C%AA%E7%9F%A5%E4%B8%BB%E9%A2%98%EF%BC%9A${subj}";
        }

        # 主题命中 Please reschedule your appointment → 调外部脚本(企业微信告警)
        # :try 保证脚本失败不影响投递;:copy 保留正常投递
        if header :contains "subject" "Please reschedule your appointment" {
            pipe :try :copy "notify.sh" ["${sender}", "${subj}", "${receiver}"];
        }
    }
}
