# SENDING MAIL BY SMTP SERVER-

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import pandas as pd
import datetime as dt
from redash_dynamic_query import RedashDynamicQuery
from http.client import IM_USED
from time import sleep, time
import win32com.client as client
from PIL import ImageGrab
import datetime, os
from datetime import date
from datetime import datetime
from datetime import timedelta

# Redash
redash = RedashDynamicQuery(
endpoint='https://redash.goibibo.com',
apikey='kdxvxHGOhFQcP5XMytV9Pn0kCzIEBk1lXS7pGpBW')
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
print("\n"+c_date)
os.chdir("C:\Reporting\Mehra Group of Hotels\Files")
query_id = 45109
result = redash.query(query_id)
gi= pd.DataFrame(result['query_result']['data']['rows'])
# using for column sequence
gi=gi[['hotelcode','hotelname','regional_head','contractmanager','city','Booking_Month','Booking_Date','bookings','RNs','RNsAAlogic','RNsAAlogicwithmax','RNsAAlogicwithroom1','GMV','PTHwithTAX','bookingvendor_id'
]]

file_name = "Mehra_Rn_" + c_date + ".csv"
gi.to_csv(file_name,index=False)

print("Redash Process Completed..\n2nd Process Start...")
os.chdir("C:\Reporting\Mehra Group of Hotels")
workbook_path = r'C:\Reporting\Mehra Group of Hotels\New_Mehra_Group_Rns - Templete-May.xlsm'
excel = client.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(workbook_path)
wb.RefreshAll()
excel.CalculateUntilAsyncQueriesDone()
wb.Save()
print("Refresh Done...")
sheet = wb.Sheets['result']
copyrange= sheet.Range('A1:N13')
copyrange.CopyPicture(Appearance=1, Format=2)
ImageGrab.grabclipboard().save('paste.png')
wb.Save()
excel.Quit()
img_path = os.getcwd() + '\\paste.png'

date_str = dt.datetime.now().strftime("%d-%b-%y %I:%M:%S %p")
print(date_str)

strFrom = 'MMT9642@go-mmt.com'
strTo = 'MMT9642@go-mmt.com'

# Create the root message 

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Mehra Group Hotels Room Night Trend '
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
# msgRoot['Cc'] =strTo          # For CC
msgRoot.preamble = 'Multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('''
Hi,<br>
Please find the attached<b style="color:red"> Mehra Group Hotels</b> room night synopsis.<br>
<div style="color:blue">This is an automated report</div>

<img src="cid:image1"><br><br>
<!-- BELOW IMAGE TEXT__! -->

<br><br>
<p>Thanks & Regards,<br>
Vineet Verma</p>
''', 'html')

msgAlternative.attach(msgText)

fp = open('C:\Reporting\Mehra Group of Hotels\paste.png', 'rb') #Read image 
msgImage = MIMEImage(fp.read())
fp.close()
# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

smtp = smtplib.SMTP('smtp.outlook.office365.com', 587)
smtp.starttls()
user_name = 'MMT9642@go-mmt.com'
paswd = "Freek7654#"
smtp.login(user_name,paswd) #Username and Password of Account
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()