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
sleep(1)

# get the path of the current working directory and create image path
image_path = os.getcwd() + '\\paste.png'
print(image_path)

# create a html body template and set the **src** property with `{}` so that we can use
# python string formatting to insert a variable
html_body = """
    <div>
          Please review the following report and response with your feedback.
    </div>
    <div>
        <img src={}></img>
    </div>
"""

# startup and instance of outlook
outlook = client.Dispatch('Outlook.Application')

# create a message
message = outlook.CreateItem(0)

# set the message properties
message.To = "vineet.verma@go-mmt.com"
message.Subject = 'Please review!'
message.HTMLBody = html_body.format(image_path)

# display the message to review
message.Display()

# save or send the message
# message.Send()