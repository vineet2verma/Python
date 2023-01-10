# Gmail send by python 

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd     # only for curr. data

date_str = pd.Timestamp().today().strftime("%d-%m-%y")

mail_content = '''
<b>Hello,</b><br>
This is a simple mail.<br> There is only text, <br>
no attachments are there The mail is sent using Python SMTP library.<br br br>

<b>Thank You<br>
Vineet Verma
</b>
'''
# Mail Addresses and Password

email_from  = 'vineet02verma@gmail.com'
password    = '#######'
email_to    = 'vineet02verma@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = "vineet02verma@gmail.com"
message['To'] = "vineet02verma@gmail.com"
message['Subject'] = 'A test mail sent by Python. It has an attachment.  '+date_str   #The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'html'))

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port

session.starttls() #enable security
session.login(email_from,password) #login with mail_id and password

# text = mail_content
text = message.as_string()
session.sendmail(email_from, email_to, text)
session.quit()
# MAIL SEND CONFIRMATION
print('Mail Sent --' + pd.Timestamp.now().strftime("%d-%m-%Y %I:%m:%s"))