#cod"ing=utf-8

import smtplib
import string

HOST = "smtp.wtest.com"
SUBJECT = "Test email from Python"
TO = "liuweijie@iiaoing.com"
CC = "zhangmei@iiaoing.com"
FROM = "liuweijie@wtest.com"
text = "Python rules them all!"

BODY = string.join((
        "From: %s " % FROM,
        "To: %s " % TO,
        "Cc: %s " % CC,
        "Subject: %s" % SUBJECT,
        "",
        text
        ),"\r\n")

server = smtplib.SMTP()
server.connect(HOST,"25")
#server.ehlo()
#server.starttls()
server.login("liuweijie@wtest.com","123.com")
server.sendmail(FROM, [TO,CC], BODY)
server.quit()