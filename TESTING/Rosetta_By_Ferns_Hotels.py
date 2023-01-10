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
apikey='kdxvxHGOhFQcP5XMytV9Pn0kCzIEBk1lXS7pGpBW')
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
print(c_date)
os.chdir("C:\Reporting\Rosetta By Ferns_Hotels\Files")
query_id = 47562
result = redash.query(query_id)
gi= pd.DataFrame(result['query_result']['data']['rows'])
gi=gi[['hotelcode','hotelname','regional_head','contractmanager','city','Booking_Month','Booking_Date','bookings','RNs','RNsAAlogic','RNsAAlogicwithmax','RNsAAlogicwithroom1','GMV','PTHwithTAX','bookingvendor_id'
]]
file_name = "Rosetta_By_Ferns_Hotels_" + c_date + ".csv"
gi.to_csv(file_name,index=False)
print("Redash Process Completed..")

def chking_func():
    # gi = pd.read_csv("c://Reporting//Rosetta By Ferns_Hotels//Files/Rosetta_By_Ferns_Hotels_2022_11_08_12_54_PM.csv")
    today = pd.to_datetime(pd.Timestamp.now().strftime('%d-%m-%Y'),format="%d-%m-%Y")    
    gi['Booking_Date'] = pd.to_datetime(gi["Booking_Date"], infer_datetime_format=True, format=('%d-%m-%Y'))
    max = gi['Booking_Date'].max()
    diff = today-max
    print(diff)
    if "2 days" in str(diff):
        print("yes")
    else:
        print("no")
        outlook = client.Dispatch("Outlook.Application")
        message = outlook.CreateItem(0)
        message.To = "vineet.verma@go-mmt.com"
        message.Subject = "Error => Rosetta By Ferns_Hotels"
        message.Cc = "vineet.verma@go-mmt.com"
        message.body = '''Hi,
            Crawlling / Redash Process is not completed ...           '''
        message.Send()
        quit()
chking_func()

# SENDING MAIL IN HTML FORMAT BY USING OUTLOOK WITH EXCEL FILE IMAGE 
print("2nd Process Start...")
os.chdir("C:\Reporting\Rosetta By Ferns_Hotels")
workbook_path = r'C:\Reporting\Rosetta By Ferns_Hotels\rosetta_By_Ferns_Hotels - Templete-Nov.xlsm'

excel = client.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(workbook_path)
wb.RefreshAll()
excel.CalculateUntilAsyncQueriesDone()
wb.Save()
sheet = wb.Sheets['result']
copyrange= sheet.Range('A1:O7')
copyrange.CopyPicture(Appearance=1, Format=2)
ImageGrab.grabclipboard().save('paste.jpg')
wb.Save()
excel.Quit()   
img_path = os.getcwd() + '\\paste.jpg'
template = '''
    <div>
    Hi,<br>
    Please find the attached<b style="color:red"> Rosetta By Ferns Hotel</b> room night synopsis.<br>
    <div style="color:blue">This is an automated report</div><br>
    {image}
    <br><br>Regards,<br>
    Vineet Verma
    </div>
'''

outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.To = "vineet.verma@go-mmt.com"
message.Subject = "Rosetta By Ferns_Hotel Room Night Trend"
message.Cc = "vineet.verma@go-mmt.com"
message.HtmlBody = template
inspector = message.GetInspector
inspector.Display()
doc = inspector.WordEditor
selection = doc.Content
selection.Find.Text = r"{image}"
selection.Find.Execute()
selection.Text = ""
img = selection.InlineShapes.AddPicture(img_path,0,1)
message.Send()
# os.remove(img_path)
print("Completed")

