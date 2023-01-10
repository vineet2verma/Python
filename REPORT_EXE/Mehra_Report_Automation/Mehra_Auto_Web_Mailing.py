# SENDING MAIL BY SMTP SERVER-

from operator import contains
import smtplib
# from email import encoders
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.image import MIMEImage
import pandas as pd
import msoffcrypto
import io
import datetime as dt
from pip import main
from pyparsing import col
from redash_dynamic_query import RedashDynamicQuery
from http.client import IM_USED
from time import sleep, time
import win32com.client as client
from PIL import ImageGrab
import datetime, os
from datetime import date
from datetime import datetime
from datetime import timedelta

file1 = 'D:\Vineet\Reporting\Mehra Group of Hotels\mail_info.xlsx'
password = ' '
temp = io.BytesIO()
with open(file1, 'rb') as f:
    excel = msoffcrypto.OfficeFile(f)
    excel.load_key(password)
    excel.decrypt(temp)
df = pd.read_excel(temp,index_col=0,sheet_name='main_info')
df = df.dropna(how='all')

user_name = df[df['From'].str.contains('@',case=False).fillna(False)]['From']
paswd = df['Pswd'].dropna(how="all").tolist()
mainsend = df[df['Send To'].str.contains('@',case=False).fillna(False)]['Send To'].tolist()
strBcc = df[df['Send Bcc'].str.contains('@',case=False).fillna(False)]['Send Bcc'].tolist()

savelocation = df['save location'][1]
query_id = int(df['query id'][1])
col_formatting = df['col formatting'].tolist()
file_name = df['file name'][1]
chg_dir = df['chg dir/path'][1]
file_path = df['file_path'][1]
sh_name1 = df['sh_name1'][1]
copy_range1 = df['copy_range1'][1]
F_attach = df['File_Attch'][1]

print()

# Redash
redash = RedashDynamicQuery(
endpoint='https://redash.goibibo.com',
apikey='kdxvxHGOhFQcP5XMytV9Pn0kCzIEBk1lXS7pGpBW')
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
print("\n"+c_date)
os.chdir(savelocation)
query_id = query_id
result = redash.query(query_id)
gi= pd.DataFrame(result['query_result']['data']['rows'])
gi=gi[col_formatting]
file_name = file_name + c_date + ".csv"
gi.to_csv(file_name,index=False)

print("Redash Process Completed..\n\n2nd Process Start...")
os.chdir(chg_dir)
workbook_path = file_path
excel = client.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(workbook_path)
wb.RefreshAll()
excel.CalculateUntilAsyncQueriesDone()
wb.Save()
sheet = wb.Sheets[sh_name1]
copyrange= sheet.Range(copy_range1)
copyrange.CopyPicture(Appearance=1, Format=2)
ImageGrab.grabclipboard().save('paste.png')
wb.Save()
excel.Quit()
img_path = os.getcwd() + '\\paste.png'

date_str = dt.datetime.now().strftime("%d-%b-%y %I:%M:%S %p")
strFrom = user_name[1]
strTo = mainsend
strBcc = strBcc
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Mehra Group Hotels Room Night Trend '
msgRoot['From'] = strFrom
msgRoot['To'] =  ",".join(strTo)
msgRoot['Cc'] = ",".join(strBcc)

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

<br><br>
<p>Thanks & Regards,<br>
Vineet Verma</p>
''', 'html')
msgAlternative.attach(msgText)

if F_attach == "Yes":
    file_path = file_path
    fileename = file_path.split("\\")[-1]
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file_path, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' %(fileename))
    msgRoot.attach(part)

fp = open('D:\Vineet\Reporting\Mehra Group of Hotels\paste.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
smtp = smtplib.SMTP('smtp.outlook.office365.com', 587)
smtp.starttls()

smtp.login(user_name[1],paswd[0])
smtp.sendmail(strFrom, (strTo+strBcc), msgRoot.as_string())
del temp
smtp.quit()