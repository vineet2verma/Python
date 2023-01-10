# SENDING MAIL BY SMTP SERVER-

import smtplib
from numpy import ndim, number
import xlwings as xw
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import openpyxl
import pandas as pd
import msoffcrypto
import io
import datetime as dt
from redash_dynamic_query import RedashDynamicQuery
from http.client import IM_USED
from time import sleep, time
import win32com.client as client
from PIL import ImageGrab
import datetime, os
from datetime import date
from datetime import datetime
from datetime import timedelta

file1 = 'C:\\Python\\Redash working\\redash_info2.xlsx'
# password = ' '
# temp = io.BytesIO()
# with open(file1, 'rb') as f:
#     excel = msoffcrypto.OfficeFile(f)
#     excel.load_key(password)
#     excel.decrypt(temp)
# df = pd.read_excel(temp)

# savelocation = df.iloc[0][1]
# query_id = df.iloc[1][1]
# col_formatting = df.iloc[2][1]
# file_name = df.iloc[3][1]

wb = openpyxl.load_workbook(file1)
sh1 = wb['Sheet1']
sh_name = wb['Sheet2']
sh2_num = wb['Sheet3']

sh_name['C2'] = "=vlookup(A2,Sheet3!a1:e10,2,0)"
sh_name['C3'] = "=vlookup(A2,Sheet3!a1:e10,2,0)"
sh_name['C4'] = "=vlookup(A2,Sheet3!a1:e10,2,0)"

xwb = xw.Book(file1)
myval = xwb.sheets['Sheet2'].range('C2:C10').options(number=int).value

sh_name.range('C2:C10').value = myval
# print(
#     sh_name['c2'].value 
# )
xwb.close()
wb.save(file1)


# # Redash
# redash = RedashDynamicQuery(
# endpoint='https://redash.goibibo.com',
# apikey='kdxvxHGOhFQcP5XMytV9Pn0kCzIEBk1lXS7pGpBW')
# c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
# print("\n"+c_date)
# os.chdir(savelocation)        
# result = redash.query(query_id)
# gi= pd.DataFrame(result['query_result']['data']['rows'])
# gi=gi[col_formatting]
# file_name = file_name + c_date + ".csv"
# gi.to_csv(file_name,index=False)
