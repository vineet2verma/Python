import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import pandas as pd
import datetime as dt
from http.client import IM_USED
from time import sleep, time
import win32com.client as client
from PIL import ImageGrab
import datetime, os
from datetime import date
from datetime import datetime
from datetime import timedelta

strFrom = 'MMT9642@go-mmt.com'
strTo = 'MMT9642@go-mmt.com'

# Create the root message 
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Subject... '
msgRoot['From'] = "supplyanalytics@makemytrip.com"
msgRoot['To'] = strTo
msgRoot.preamble = 'Multi-part message in MIME format.'
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('''
Hi,<br>
Please find the attached<b style="color:red"> Mehra Group Hotels</b> room night synopsis.<br>

<br><br>
<p>Thanks & Regards,<br>
Vineet Verma</p>
''', 'html')

msgAlternative.attach(msgText)
fp = open('C:\Reporting\Rosetta By Ferns_Hotels\paste.jpg', 'rb') #Read image 
msgImage = MIMEImage(fp.read())
fp.close()
# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

smtp = smtplib.SMTP('smtp.outlook.office365.com', 587)
smtp.starttls()
user_name = 'MMT9642@go-mmt.com'
paswd = "sgbpryswdhxqcltz"

smtp.login(user_name,paswd) #Username and Password of Account
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
