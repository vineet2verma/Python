from cgitb import html
from email import message
import win32com.client as client
outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.display()
message.send()


# message.from = "vineet.verma@go-mmt.com"
message.To = "vineet.verma@go-mmt.com"
message.Subject = "This is Subject Text"
message.Body = "Body Text Here"
message.htmlbody = '''
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <img src="C:\CHKING/MEHRA REPORT/paste.png" width="60%" height="30%"></src>
       <br><br>
       has many great tutorials.
    </p>
  </body>
</html>
'''


