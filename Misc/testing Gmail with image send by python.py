# Gmail send by python 

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import pandas as pd
from requests import session     # only for curr. data

date_str = pd.Timestamp.today().strftime("%d-%m-%Y")

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
password    = '#####'
email_to    = 'amit2srivastav@gmail.com'

#Create SMTP session for sending the mail

# FOR SMTP USING PORT 587 
with smtplib.SMTP('smtp.gmail.com', 587) as session: #use gmail with port
    session.ehlo()  # ehlo is alternative to helo for services that support the smtp services ext.
    session.starttls() #enable security
    session.ehlo()

# FOR SMTP_SSL PORT 465 ( ECLO IS NOT REQ. IT'S SIMPLE METHOD )
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as session:    #use gmail with port

    session.login(email_from,password)                      #login with mail_id and password

    # subject = 'Subject Body '
    # body = 'This is Body Text '
    # msg = f'Subject : {subject}\n\n{body}'
    # session.sendmail(email_from, email_to, msg)


                                    # THIS IS ALSO WORKING
#Setup the MIME

message = MIMEMultipart()
message['From'] = "vineet02verma@gmail.com"
message['To'] = "vineet02verma@gmail.com"
message['Subject'] = 'A test mail sent by Python. It has an attachment.  '+date_str   #The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'html'))

# text = mail_content
text = message.as_string()
session.sendmail(email_from, email_to,text)
session.quit()

# MAIL SEND CONFIRMATION
print('Mail Sent --' + pd.Timestamp.now().strftime("%d-%m-%Y %I:%m:%s"))




