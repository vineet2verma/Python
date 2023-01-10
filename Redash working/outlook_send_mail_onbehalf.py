
#  NOT COMPLETED AS PER OUR EXPECTATION............

# import win32com.client as win32

# def send_email(sender,recipient):
#     outlook = win32.Dispatch('outlook.application')
#     # mail = outlook.CreateItem(0)
#     # mail.To = recipient
#     # mail.Subject = "Test Emails"
#     # mail.HTMLBody = "Test Content"
#     # mail.SendUsingAccount = sender
#     # mail.Display()

#     for ou in outlook.Session.Accounts:
#         print(ou)

# recipient = "vineet.verma@go-mmt.com"
# sender= "SupplyAnalytics@makemytrip.com"

# send_email(sender,recipient)


from itertools import count
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

for acc in outlook.Session.Accounts:
    print (acc)




