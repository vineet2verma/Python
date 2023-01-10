# https://redash.goibibo.com/queries/41894/source?p_Start%20Date=2022-06-01&p_End%20Date=2022-06-30 # Pankaj Query

from dataclasses import replace
from operator import index
from statistics import mode
import pandas as pd
import xlwings as xw
import numpy as np
import warnings
import smtplib, openpyxl
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from matplotlib.pyplot import text
import matplotlib.pyplot as plt
import msoffcrypto
import io
import datetime as dt
from redash_dynamic_query import RedashDynamicQuery
from http.client import IM_USED
from time import sleep, time
from requests import head
import win32com.client as client
from PIL import ImageGrab
import datetime, os
from datetime import date
from datetime import datetime
from datetime import timedelta

file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\RNs_data#Recovery_growth_-_CheckIn_2022_10_29 (2).csv'
mapping_file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\Mapping.xlsx'
df1 = pd.read_csv(file)
df2 = pd.read_excel(mapping_file,sheet_name='Data')
df = pd.merge(left=df1,right=df2,left_on='hotelcode',right_on="Hotelcode",how="right")
print("\n- - START - - \n")
print(df.columns)

df = df[df.TEAM.isin(['NICE','SWAG'])] 
df['Booking_Date'] = pd.to_datetime(df['Booking_Date'])
df['day'] = df.Booking_Date.dt.day
max_day = df['Booking_Date'].max()


print("\n- - END - - \n")

df = df.loc[(df['Booking_Date'] > "2022-06-25") & (df['Booking_Date'] <= "2022-06-30")]
df.columns = df.columns.str.replace(' ','_')

unique_rm = []
for i in df.RM_Name.unique(): unique_rm.append(i)

rm = df.groupby(['RM_Name'])['RNs'].sum()
print(rm)
zm = df.groupby(['RM_Name','ZM_Name'])['RNs'].sum()
print(zm)
bdm = df.groupby(['RM_Name','ZM_Name','BDM_Name'])['RNs'].sum()
print(bdm)

# for i in range(0,5):
#     group_ = df.query("RM_Name =='{rm}'".format(rm = unique_rm[i])).groupby(['day'])['RNs'].sum()
#     pic = group_.plot(kind='pie',xlabel="No's of Days",ylabel='Room Night',title = unique_rm[i].upper()).get_figure()    
#     pic.savefig('c:\\Python\\img_0'+str([i]))
#     plt.show()




        # DF TO MAIL BODY IN TABLE FORMAT
# outlook = win32.Dispatch('Outlook.Application')
#     ''' ''' + df_10.to_html(index=False) + ''' <img src="'''+ pic_save +'''">  '''
#     + df_10.to_html(index=False) +

# body = '''
# <html>
#     <body>
#         <div class = "container">
#             <div class = "inner_img">
#                           ''''''<br>
#             </div>
#             <div>
#                 <img src='C:\Python\img1.jpg'>    <img src='C:\Python\img1.jpg'>
#             </div>
#             <div>
#                 '''+ df_10.to +'''
#             </div>
#         </div>
#     </body>
# </html>
# '''
# mail = outlook.CreateItem(0)
# mail.Subject = "This subject line"
# mail.To = 'vineet.verma@go-mmt.com'
# mail.HTMLBody = body
# mail.Display()
# # mail.Send()