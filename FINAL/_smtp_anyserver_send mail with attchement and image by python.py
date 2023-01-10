# SEND MAIL BY SMTP 
# HTML FORMAT,
# IMAGE BY LOCATION, ATTACHMENT BY LOCATION

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import datetime as dt

date_str = dt.datetime.now().strftime("%d/%m/%y %I:%M %p")
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

file_path = "C:\\CHKING\\002.xlsx"
fileename = file_path.split("\\")[-1]
part = MIMEBase('application', "octet-stream")
part.set_payload(open(file_path, "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="%s"' %(fileename))

msgRoot.attach(part)

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
username    = 'vineet02verma@gmail.com'
password    = '********'
smtp.login(username, password) #Username and Password of Account
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()