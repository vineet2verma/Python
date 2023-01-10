import pandas as pd
import numpy as np
import datetime, os
from datetime import date
from datetime import datetime
from datetime import timedelta
import requests, json, csv
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from redash_dynamic_query import RedashDynamicQuery

from http.client import IM_USED
from time import sleep, time
import win32com.client as client
from PIL import ImageGrab

# https://redash.goibibo.com/queries/47562/source

redash = RedashDynamicQuery(
endpoint='https://redash.goibibo.com',
apikey='kdxvxHGOhFQcP5XMytV9Pn0kCzIEBk1lXS7pGpBW'
)
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
print(c_date)
os.chdir("C:\Reporting\Rosetta By Ferns_Hotels\Files")
print(os.getcwd())
query_id = 47562
result = redash.query(query_id)
gi= pd.DataFrame(result['query_result']['data']['rows'])
# using for column sequence
gi=gi[['hotelcode','hotelname','regional_head','contractmanager','city','Booking_Month','Booking_Date','bookings','RNs','RNsAAlogic','RNsAAlogicwithmax','RNsAAlogicwithroom1','GMV','PTHwithTAX','bookingvendor_id'
]]
print( os.getcwd())
file_name = "Rosetta_By_Ferns_Hotels_" + c_date + ".csv"
gi.to_csv(file_name,index=False)
print( os.getcwd())
print("Redash Process Completed..")
# SENDING MAIL IN HTML FORMAT BY USING OUTLOOK WITH EXCEL FILE IMAGE 
# OPEN EXCEL & REFRESH LAST MODIFIED DATE DATA 
# LASTLY REMOVE THAT IMAGE

# print("2nd Process Start...")
# os.chdir("C:\Reporting\Mehra Group of Hotels")
# workbook_path = r'C:\Reporting\Mehra Group of Hotels\New_Mehra_Group_Rns - Templete-May.xlsm'

# excel = client.Dispatch('Excel.Application')
# wb = excel.Workbooks.Open(workbook_path)
# wb.RefreshAll()
# excel.CalculateUntilAsyncQueriesDone()
# wb.Save()
# print("Refresh Done...")
# sheet = wb.Sheets['result']
# copyrange= sheet.Range('A1:N13')
# copyrange.CopyPicture(Appearance=1, Format=2)
# # grab the saved image from the clipboard and save to working directory
# ImageGrab.grabclipboard().save('paste.png')
# wb.Save()
# excel.Quit()   

# get the path of the current working directory and create image path
# image_path = os.getcwd() + '\\paste.png'
img_path = os.getcwd() + '\\paste.png'
print("Outlook Process Start...")
template = '''
    <div>
    Hi,<br>
    Please find the attached<b style="color:red"> Mehra Group Hotels</b> room night synopsis.<br>
    <div style="color:blue">This is an automated report</div><br>
    {image}
    <br><br>Regards,<br>
    Vineet Verma
    </div>
'''

outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.From = "SupplyAnalytics@makemytrip.com"
message.To = "Vikram.Challur@go-mmt.com; Shino.Baby@go-mmt.com; tahir.khatri@go-mmt.com"
message.Subject = "Mehra Group Hotels Room Night Trend"
message.Cc = "jayant.malik@go-mmt.com; SupplyAnalytics@makemytrip.com"
message.Bcc = "vineet.verma@go-mmt.com"
message.HtmlBody = template

inspector = message.GetInspector
inspector.Display()
message.Display()
doc = inspector.WordEditor
selection = doc.Content
selection.Find.Text = r"{image}"
selection.Find.Execute()

selection.Text = ""
img = selection.InlineShapes.AddPicture(img_path,0,1)
os.remove(img_path)
print("Completed")