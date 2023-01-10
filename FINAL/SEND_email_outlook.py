from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.message import Message
from email import encoders
import os
import json
from email.mime import message
import smtplib as s
from certifi import contents
from pretty_html_table import build_table


localhost = "smtp.gmail.com"
ob = s.SMTP(localhost, 587)
ob.starttls()
username = "vineet02verma@gmail.com"
password = "#######"
ob.login(username, password)

content = open('config/gmail.json')
config = json.load(content)
print(config[username])
email =  config["email"]  
# print(email)

# message= (f"Subject:{subject}\n\n{html_body}")
# print(message)  # for chking message

list_of_msg = []
list_of_msg.append(username)
# list_of_msg.append("vineet2verma@gmail.com") 

# for sending msg
# ob.sendmail(username,list_of_msg,message)
# ob.quit()
# print("Email Send Sucessfully to ",list_of_msg)