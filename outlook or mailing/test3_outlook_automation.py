# OUTLOOK MAIL FIND : SUBJECT BASIS MATCH , SENDER BASIS MATCH 

from ast import If
from email.policy import strict
import win32com.client
import os
from datetime import datetime, timedelta
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
# for account in mapi.Accounts:
#     print(account.DeliveryStore.DisplayName) #outlook account
inbox = mapi.GetDefaultFolder(6) #Inbox folder
# inbox = inbox.Folders["Inbox"] #Folder inside Inbox Folder
messages = inbox.Items 
received_dt = datetime.now() - timedelta(days=2)
received_dt = received_dt.strftime('%d/%m/%Y')
print(received_dt)
sender1 = 'Rishi Sharma'
sender2 = "rishi.sharma@go-mmt.com"
f_subj = 'room x'
messages = messages.Restrict("[ReceivedTime] >= '"+received_dt+"'")
messages.sort("[ReceivedTime]",True)
date_ = datetime.now().strftime('%Y-%m-%d')

#save to current directory

for message in list(messages):
    # print(f"{message.sender}\t{message.ReceivedTime.strftime('%Y-%m-%d %I:%M %p')}\t{message.subject}")
    if str(message.sender) == str(sender1) or str(message.sender) == str(sender1):
        # print("\nSender Found\n")
        # print(f"{message.sender}\t{message.ReceivedTime.strftime('%Y-%m-%d %I:%M %p')}\t{message.subject}")
        # if email_subject == message.subject:

        if message.subject.lower().find(f_subj) != -1:
            # aa = message.subject.lower().index("x")  # also work
            print(f"{message.sender}\t{message.ReceivedTime.strftime('%Y-%m-%d %I:%M %p')}\t{message.subject}")
            if message.ReceivedTime.strftime('%Y-%m-%d') >= received_dt:
                print("Time Found")







# import win32com.client
# import time
# from datetime import datetime, timedelta

# outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
# received_dt = datetime.now() - timedelta(days=5)
# received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')

# frm__ = "Rishi Sharma"
# sub__ = "Room X Meal Plan Datafile"

# inbox = outlook.GetDefaultFolder(6)     # inbox 
# msgs = inbox.Items
# msgs.sort("[ReceivedTime]",True)

# for row,msg in enumerate(msgs):
#     frm = msg.SenderName
#     sen_time = msg.ReceivedTime.strftime("%m/%d/%Y %H:%M")
#     subject = msg.Subject
#     body = msg.Body
#     attachs = msg.Attachments
#     print(f"{row}:\t{sen_time}\t{frm}\t{subject}")
 

    # # for index,attch in enumerate(attachs):
    #     # att_li = att_li.append(attch(index))
   
    # attach1 = attachs.Item(1)     # FOR SINGLE FILE 
    # att_li = attach1.FileName
    # if frm.find("Rishi Sharma") :
    # # if subject == subj and frm == frm2_:
    #     print(f"\nFrom: {frm}\nSub: {subject}\nRecd_time: {sen_time}\nAttchment: {att_li}")
    
