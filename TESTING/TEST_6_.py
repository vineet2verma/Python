# SENDING MAIL IN HTML FORMAT WITH IMAGE ( EXCEL DATA IMAGE ). AND LASTLY REMOVE THAT USED IMAGE

from http.client import IM_USED
import os
from time import sleep, time
import win32com.client as client
from PIL import ImageGrab

os.chdir("C:\CHKING\MEHRA REPORT")
# make sure you use either a raw string OR escape characters for the backslash. 
# You CANNOT use forward slash format with `win32com`.
workbook_path = r'C:/CHKING/MEHRA REPORT/Mehra Group of Hotels Trends - Templete - April.xlsm'

# start an instance of Excel
excel = client.Dispatch('Excel.Application')

# open the workbook
wb = excel.Workbooks.Open(workbook_path)

#  Refreshing All Sheets
wb.Refresh.All()
wb.Save()

# select the sheet you want... use whatever index method you want to use....

### by item
# sheet = wb.Sheets.Item(1)

### by index
# sheet = wb.Sheets[0]

### by name
sheet = wb.Sheets['result']

# copy the target range
copyrange= sheet.Range('A1:N13')
copyrange.CopyPicture(Appearance=1, Format=2)

# grab the saved image from the clipboard and save to working directory
ImageGrab.grabclipboard().save('paste.png')
excel.quit()   
# sleep(1)

# get the path of the current working directory and create image path
# image_path = os.getcwd() + '\\paste.png'
img_path = os.getcwd() + '\\paste.png'

template = '''
    <p>Hi,<br>
    please find the attached <b style="color:red"><u>Mehra Group Hotels</u></b> room night synopsis.
    <p style="color:blue;font-size:11px">This is an automated report</p><br><br>

    {image}
       
    <br><br>Regards,<br>
    Vineet Verma
    </p>
'''

outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.To = "vineet.verma@go-mmt.com"
message.Subject = "Mehra Group Hotels Room Night Trend"
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
