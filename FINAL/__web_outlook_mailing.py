# SEND MAIL BY SERVER
# HTML FORMAT

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import smtplib
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

email_user = 'MMT9642@go-mmt.com'
email_password = "#######" # str(input("Enter password :   "))
email_send = "MMT9642@go-mmt.com"

email_cc="MMT9642@go-mmt.com"
email_sender = "MMT9642@go-mmt.com"

msg = MIMEMultipart()
msg['Subject'] = "Chking for Automation"
msg['From'] = email_user
msg['Sender']=email_sender
msg['To'] = email_send
msg["Cc"]=email_cc
msg['Password']=email_password

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
"""

html = '''\
<html>
  <body>
    <p>Hi,<br><br>
       Please find the attached <b>Mehra Group Hotels</b> room night synopsis<br>
       <u>This is an automated report</u><br>
       
       Regards,<br>
       Vineet Verma
    </p>
  </body>
</html>
'''

# Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# The email client will try to render the last part first
# msg.attach(part1)
msg.attach(part2)

server = smtplib.SMTP('smtp.outlook.office365.com',587)
server.starttls()
server.login(msg['From'],msg['Password'])
server.sendmail(msg['Sender'], msg['To'].split(",")+msg['Cc'].split(","), msg.as_string())
server.quit()
print('email send sucessfully to,', email_send)