'''
武沛齐博客园->python之路->python开发第一篇
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('博士必上', 'plain', 'utf-8')
msg['From'] = formataddr(("刘总", 'liuz210206@163.com'))
msg['To'] = formataddr(("刘秀达", '1369578672@qq.com'))
msg['Subject'] = "你准备读博嘛？"

server = smtplib.SMTP("smtp.163.com", 25)
server.login("liuz210206@163.com", "lzlz210206...")
server.sendmail('liuz210206@163.com', ['1369578672@qq.com', ], msg.as_string())
server.quit()