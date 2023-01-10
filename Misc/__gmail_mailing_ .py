# SEND MAIL BY GMAIL SERVER

from email.mime import message
from http import server
import smtplib as S

from matplotlib.style import context

username = "vineet02verma@gmail.com"
password =  "#######"                    # str(input("Enter Your password"))

localhost = "smtp.gmail.com"
ob = S.SMTP(localhost, 587)
ob.starttls()
ob.login(username, password)

subject = "sending email using python"
body =  "This is body text sending msg by using python"

html_body = '''
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
'''

message= (f"Subject:{subject}\n\n{html_body}")
print(message)  # for chking message

list_of_msg = []
list_of_msg.append(username)
list_of_msg.append("vineet2verma@gmail.com")

# for sending msg
  ob.sendmail(username,list_of_msg,message)  
  ob.quit()
  print("Email Send Sucessfully to ",list_of_msg)