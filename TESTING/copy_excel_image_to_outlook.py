import os
from turtle import width
from openpyxl import Workbook
import win32com.client as client
from PIL import ImageGrab
os.chdir('C:\\CHKING\\MEHRA REPORT\\')
workbook_path = os.getcwd() + '\\Mehra Group of Hotels Trends - Templete - April.xlsm'

excel = client.Dispatch("Excel.Application")
wb = excel.workbooks.Open(workbook_path)
sheet = wb.sheets['mail body']
excel.visible = 1
range = 'C9:P20'
copyrange = sheet.Range(range)
copyrange.CopyPicture(Appearance=1, Format=2)
ImageGrab.grabclipboard().save('paste.png')
excel.Quit()

image_path = os.getcwd() + '\\paste.png'
print(image_path)
html_body = '''
<div>
    This is a demo of image grab <br><br>
</div>
<div>
    <img src = {} ></img>
</div>

'''

outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.To = "abc@go-mmt.com"
message.Subject = "Chiking Image"
message.HtmlBody = html_body.format(image_path)
message.Display()