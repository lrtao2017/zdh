#cod"ing=utf-8

import smtplib
from email.mime.text import MIMEText

HOST = "smtp.wtest.com"
SUBJECT = "官网流量数据报表"
TO = "liuweijie@iiaoing.com"
CC = "liuweijie@wtest.com"
FROM = "liuweijie@wtest.com"

msg = MIMEText("""
      <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
          <td bgcolor="#CECFAD" height="20" style="font-size:14px">* guangwang shuju <a
          href="www.baidu.com" > more >></a></td>
      </tr>
      <tr>
          <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
           1)Daily_vists:<font color=red>152433</font> 
             Visits:23651 Page_views:45123 Clicks:545122 Data_flow:504MB<br>
           2)Status code information<br>
             &nbsp;&nbsp;500:105  404:3264 503:214<br>
           3)Guest browser information<br>
             &nbsp;&nbsp; IE:50% firefox:10% chrome:30% other:10%<br>
           4)Page information<br>
             &nbsp;&nbsp;/index.php 42153<br>
             &nbsp;&nbsp;/view.php 21451<br>
             &nbsp;&nbsp;/login.php 5112<br>
          </td>
      </tr>
      </table>""","html","utf-8")

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
msg['Cc'] = CC

try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    #server.ehlo()
    #server.starttls()
    server.login("liuweijie@wtest.com","123.com")
    server.sendmail(FROM, [TO,CC], msg.as_string())
    server.quit()
    print "Sent OK"
except Exception, e:
    print "Sent Failed:"+str(e)
