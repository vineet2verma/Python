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

file1 = 'C:/Reporting/Neo Chains/Redash_Neo_info.xlsx' # information 
df = pd.read_excel(file1,engine='openpyxl',index_col=0)
savelocation = df.iloc[0][0]
query_id = df.iloc[1][0]
col_formatting = df.iloc[2].tolist()
file_name = df.iloc[3][0]


file4 = 'c:/Python/Redash working/NEO FILE/Neo_Rn_2022_07_14_03_20_PM.csv'  # 
file3 = 'c:/Python/Redash working/test.xlsx'                                # clean & data paste file

# wb = openpyxl.load_workbook(file3)
# sh = wb['RN2']
# lrow = sh.max_row
# #  data clean
# for row in sh['A2:O'+str(lrow)]:
#     for cell in row:
#         cell.value = ""


# df4 = pd.read_csv(file4)

# NOT COMPLETED YET NOW................

wb = xw.Book(file3)
sh = wb.sheets['RN2']
lrow = sh.range("A2").current_region.last_cell.row
print = lrow
# sh['A2:O'].value = ""
# sh['A2'].value = df4.values


# sh.range('P2:Q100').formula = sh.range('P2:Q2').formula
# # range('RN2','P3:Q100').value = formula1

wb.close
# wb.save
print("done")






