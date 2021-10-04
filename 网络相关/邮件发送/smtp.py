#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

sender = "python@nooob.top"
sender_name = "Python"
passwd = "大小一二到五点"
to_user = "duyun888888@qq.com"
to_user_name = "DY"
smtp_server = "smtp.exmail.qq.com"
smtp_server_port = 465

title = "Title"
text = "TEXT"

pattern_choose = input("Please input pattern(plain-1, html-2)：")
if pattern_choose == '1':
    pattern = "plain"
elif pattern_choose == '2':
    pattern = "html"
else:
    print("Unknow pattern.")

title = input("Title, please:")
text = input("Text({}), please:".format(pattern))


def mail():
    global sender, sender_name, to_user, passwd, smtp_server, smtp_server_port, title, text, pattern
    result = True
    try:
        msg = MIMEText(text, pattern, 'utf-8')
        msg['From'] = formataddr([sender_name, sender])
        msg['To'] = formataddr([to_user_name, to_user])
        msg['Subject'] = title

        server = smtplib.SMTP_SSL(smtp_server, smtp_server_port)
        server.login(sender, passwd)
        server.sendmail(sender, [to_user, ], msg.as_string())
        server.quit()
    except:
        result = False
    return result


ret = mail()
if ret:
    print("Send [success]")
else:
    print("Send [failed]")
