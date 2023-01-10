# SEND MAIL BY SERVER
# HTML FORMAT 
# WITH IMAGE BY LOCATION


import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import pandas as pd

date_str = pd.Timestamp().now().strftime('%d-%M-%Y %I:%m:%s')
print(date_str)

strFrom = 'vineet02verma@gmail.com'
strTo = 'vineet02verma@gmail.com'

# Create the root message 

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'SUBJECT HERE '
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
# msgRoot['Cc'] =strTo
msgRoot.preamble = 'Multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('''
<b>HTML BODY TEXT HERE </b> and an image.<br><br><br>

<img src="cid:image1"><br><br>

BELOW IMAGE TEXT__!

<br><br>
<p>Thanks & Regards,<br>
Vineet Verma</p>
''', 'html')

msgAlternative.attach(msgText)

#Attach Image 
fp = open('c:\image1.jpg', 'rb') #Read image 
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

import smtplib
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
# smtp.connect('smtp.gmail.com') #SMTp Server Details
username = 'vineet02verma@gmail.com'
password = '$$$$$$$$'
smtp.login(username,password) #Username and Password of Account
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()