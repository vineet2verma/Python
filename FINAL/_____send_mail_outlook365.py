# SENDING MAIL BY SMTP SERVER-
# WITH IMAGE BY LOCATION PATH AND ATTACHMENT BY LOCATION PATH .

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import pandas as pd
import msoffcrypto
import io
import datetime as dt

file1 = 'D:\Vineet\Reporting\Mehra Group of Hotels\mail_info.xlsx'
password = ' '
temp = io.BytesIO()
with open(file1, 'rb') as f:
    excel = msoffcrypto.OfficeFile(f)
    excel.load_key(password)
    excel.decrypt(temp)
df = pd.read_excel(temp)
user_name = df.iloc[0][0]
paswd = df.iloc[0][1]
del temp



date_str = dt.datetime.now().strftime("%d-%b-%y %I:%M:%S %p")
print(date_str)

strFrom = 'MMT9642@go-mmt.com'
strTo = ['MMT9642@go-mmt.com','vineet.verma@go.mmt.com']
strTo = ",".join(strTo)
# Create the root message 

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'SUBJECT HERE '
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
# msgRoot['Cc'] =strTo          # For CC
msgRoot.preamble = 'Multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('''
<b>HTML BODY TEXT HERE </b> and an image.<br><br><br>

<img src="cid:image1"><br><br>
<!-- BELOW IMAGE TEXT__! -->

<br><br>
<p>Thanks & Regards,<br>
Vineet Verma</p>
''', 'html')

msgAlternative.attach(msgText)


#  FOR FILE ATTACHMENT START
    # file_path = "C:\\CHKING\\002.xlsx"
    # fileename = file_path.split("\\")[-1]
    # part = MIMEBase('application', "octet-stream")
    # part.set_payload(open(file_path, "rb").read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', 'attachment; filename="%s"' %(fileename))
    # msgRoot.attach(part)
#  FILE FILE ATTACHMENT END

#Attach Image Start  ( Used This In Html Tagging :- <img src="cid:image1"> )
fp = open('d:\Vineet\Reporting\Mehra Group of Hotels\paste.png', 'rb') #Read image 
msgImage = MIMEImage(fp.read())
fp.close()
# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
# Attach Image End


smtp = smtplib.SMTP('smtp.outlook.office365.com', 587)
smtp.starttls()
# user_name = 'MMT@go-mmt.com'
# paswd = "Fre#"
smtp.login(user_name,paswd) #Username and Password of Account
smtp.sendmail(strFrom, (strTo), msgRoot.as_string())
smtp.quit()


