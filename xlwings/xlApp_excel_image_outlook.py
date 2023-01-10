# testing  not working

xlApp = win32.DispatchEx('Excel.Application')
wb = xlApp.Workbooks.Open('c:/CHKING/MEHRA REPORT/Mehra Group of Hotels Trends - Templete - April.xlsm')
ws = wb.Worksheets('mail body')

win32c = win32.constants
ws.Range("C9:P20").CopyPicture(Format=win32c.xlBitmap)
img = ImageGrab.grabclipboard()
img.save('C:/CHKING/MEHRA REPORT/paste.png', quality=95)
wb.Close()

pdf_path = 'C:/CHKING/MEHRA REPORT/paste.pdf'
image = Image.open('C:/CHKING/MEHRA REPORT/paste.png')
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()

image_path = 'C:/CHKING/MEHRA REPORT/paste.png'
html_body = """
    <div>
        Hello Marcus,<br>
        <br>
        Data below<br>
    </div>
    <div>
        <img src={}></img>
    </div>
"""

outlook = win32.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)
message.To = ''
message.Subject = 'Daily Production Numbers'
message.HTMLBody = html_body.format(image_path)
message.Display()