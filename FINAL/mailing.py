# MAILING WITH FILE ATTACHMENT BY LOCATION
# BODY IN PLAIN TEXT

from posixpath import splitext
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

username = "MMT9642@go-mmt.com"
password = "******"

mail_from = "vineet.verma@go-mmt.com"
mail_to = "vineet.verma@go-mmt.com"
mail_subject = "Test Subject"
mail_body = "This is a test message"
# mail_attachment="https://d1ny9casiyy5u5.cloudfront.net/tmp/test.txt"
mail_attachment="C:/CHKING/002.xlsx"

mail_attachment_name= mail_attachment.split("/")[-1]

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))

with open(mail_attachment, "rb") as attachment:
    mimefile = MIMEBase('application', 'octet-stream')
    mimefile.set_payload((attachment).read())
    encoders.encode_base64(mimefile)
    mimefile.add_header('Content-Disposition', "attachment; filename= %s" % mail_attachment_name)
    mimemsg.attach(mimefile)
    connection = smtplib.SMTP(host='smtp.outlook.office365.com', port=587)
    connection.starttls()
    connection.login(username,password)
    connection.send_message(mimemsg)
    connection.quit()