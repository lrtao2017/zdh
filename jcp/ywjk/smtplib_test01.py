#cod"ing=utf-8

import smtplib
import string

HOST = "smtp.wltest.com"
SUBJECT = "Test email from Python"
TO = "liuweijie@itiaoling.com"
CC = "zhangmei@itiaoling.com"
FROM = "liuweijie@wltest.com"
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
server.login("liuweijie@wltest.com","Rfd123.com")
server.sendmail(FROM, [TO,CC], BODY)
server.quit()