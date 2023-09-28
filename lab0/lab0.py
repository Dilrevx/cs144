# from pwn import *
# context.log_level = 'debug'

# EAddrQQ = '1747693932@qq.com'
# smtp = f'''
# HELO k
# AUTH login
# ZGFhdDAwQHNqdHUuZWR1LmNu
# aGUyMDAyMTQ=
# MAIL FROM: daat00@sjtu.edu.cn
# RCPT TO: {EAddrQQ}
# DATA
# From: daat00@sjtu.edu.cn
# To: {EAddrQQ}
# Subject: Test!
# Test email from python!
# .
# QUIT
# '''

# conn = connect('mail.sjtu.edu.cn', 25)
# conn.recvline()
# for line in smtp.strip().split('\n'):
#     if line == '.':
#         line = '\r\n.\r\n'
#     else:
#         line += '\n'

#     sleep(0.5)
#     conn.send(line)
#     conn.recvline(timeout=1)


'''
Another Method
'''

import smtplib
import base64
from email.mime.text import MIMEText

# 邮件服务器的地址和端口
smtp_server = 'smtp.sjtu.edu.cn'
smtp_port = 25

# 发件人和收件人的邮箱地址
sender_email = 'daat00@sjtu.edu.cn'
receiver_email = '1747693932@qq.com'

# 邮件内容
subject = 'TEST!'
body = '这是一封通过 Python 发送的邮件'

# 构造 MIMEText 对象
message = MIMEText(body, 'plain')
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

# 连接到 SMTP 服务器并发送邮件
with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
    server.login(sender_email,
                 'he200214')  # 发件人邮箱的登录密码
    server.sendmail(sender_email, receiver_email, message.as_string())

print('邮件发送成功')
