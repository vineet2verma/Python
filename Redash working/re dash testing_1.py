# SENDING MAIL BY SMTP SERVER-

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

file1 = 'C:\\Reporting\\TESTING\\Redash_info.xlsx' # information 
df = pd.read_excel(file1,engine='openpyxl',index_col=0)
savelocation = df['save location'][1]
query_id = 37742
col_formatting = df['col formatting'].tolist()
file_name = df['file name'][1]

# Redash
redash = RedashDynamicQuery(
endpoint='https://redash.goibibo.com',
apikey='kdxvxHGOhFQcP5XMytV9Pn0kCzIEBk1lXS7pGpBW')
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
print("\n"+c_date)
os.chdir(savelocation)        
print(savelocation)

result = redash.query(query_id)

gi= pd.DataFrame(result['query_result']['data']['rows'])
gi=gi[col_formatting]
file_name = file_name + c_date + ".csv"
gi.to_csv(file_name,index=False)


# file4 = 'c:/Python/Redash working/NEO FILE/Neo_Rn_2022_07_14_03_20_PM.csv'
# file3 = 'c:/Python/Redash working/test.xlsx'    # data paste file
# wb = openpyxl.load_workbook(file3)
# sh = wb['RN2']
# lrow = sh.max_row
# #  data clean
# for row in sh['A2:O'+str(lrow)]:
#     for cell in row:
#         cell.value = ""

# df4 = pd.read_csv(file4)
# wb = xw.Book(file3)
# sh = wb.sheets['RN2']
# sh['A2'].value = df4.values

# sh.range('P2:Q100').formula = sh.range('P2:Q2').formula
# # range('RN2','P3:Q100').value = formula1

# wb.save
print("done")






