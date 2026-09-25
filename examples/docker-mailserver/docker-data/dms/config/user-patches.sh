#!/bin/bash
# docker-mailserver 启动时执行。定义慢速 transport,给发往 QQ/163 的邮件限速。

# 新建 master.cf 服务:slow(基于 smtp 投递代理)
postconf -Me "slow/unix=slow unix - - n - - smtp"

# 该服务的限速参数
postconf -P "slow/unix/syslog_name=postfix-slow"
postconf -P "slow/unix/smtp_destination_rate_delay=60s"
postconf -P "slow/unix/smtp_destination_concurrency_limit=1"
