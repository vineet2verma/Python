import win32com.client
import time
from datetime import datetime, timedelta

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
received_dt = datetime.now() - timedelta(days=2)
received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
print(received_dt)
# root_folder = outlook.Folders.Item(2)
#  Get All Folder Name
# for index,folder in enumerate(root_folder.Folders):
#     print(folder.Name)

frm__ = "Rishi Sharma"     # Anjani nedunuri
frm2_ = "Anjani nedunuri"
subj = "Room X Meal Plan Datafile"

inbox = outlook.GetDefaultFolder(6)     # inbox 

msgs = inbox.Items
att_li = []

print(len(att_li))


for msg in msgs:
    frm = msg.SenderName
    sen_time = msg.ReceivedTime.strftime("%d_%m_%Y")
    subject = msg.Subject
    body = msg.Body
    attachs = msg.Attachments
    # for index,attch in enumerate(attachs):
        # att_li = att_li.append(attch(index))
    
    
    attach1 = attachs.Item(1)     # FOR SINGLE FILE 
    att_li = attach1.FileName
    if frm.find("Rishi Sharma") :
    # if subject == subj and frm == frm2_:
        print(f"\nFrom: {frm}\nSub: {subject}\nRecd_time: {sen_time}\nAttchment: {att_li}")
    
