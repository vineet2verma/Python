# SENDING MAIL IN HTML FORMAT BY USING OUTLOOK WITH EXCEL FILE IMAGE 
# OPEN EXCEL & REFRESH LAST MODIFIED DATE DATA 
# LASTLY REMOVE THAT IMAGE

from http.client import IM_USED
import os
from time import sleep, time
import win32com.client as client
from PIL import ImageGrab
print("Process Start...")
os.chdir("C:\Reporting\Mehra Group of Hotels")
# make sure you use either a raw string OR escape characters for the backslash. 
# You CANNOT use forward slash format with `win32com`.
workbook_path = r'C:\Reporting\Mehra Group of Hotels\New_Mehra_Group_Rns - Templete-May.xlsm'

# start an instance of Excel
excel = client.Dispatch('Excel.Application')
# open the workbook
wb = excel.Workbooks.Open(workbook_path)
# Refresh all data connections.
wb.RefreshAll()
excel.CalculateUntilAsyncQueriesDone()
wb.Save()
print("Refresh Done...")
# by name
sheet = wb.Sheets['result']
# copy the target range
copyrange= sheet.Range('A1:N13')
copyrange.CopyPicture(Appearance=1, Format=2)

# grab the saved image from the clipboard and save to working directory
ImageGrab.grabclipboard().save('paste.png')
wb.Save()
excel.Quit()   

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
message.To = "Vikram.Challur@go-mmt.com; Shino.Baby@go-mmt.com; tahir.khatri@go-mmt.com"
message.Subject = "Mehra Group Hotels Room Night Trend"
message.Cc = "jayant.malik@go-mmt.com"
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