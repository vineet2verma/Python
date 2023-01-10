from cProfile import label
from cgi import print_arguments
from email.header import Header
from fileinput import filename
from gettext import find
from inspect import stack
from itertools import count
from operator import index
from pickle import TRUE
from textwrap import indent
from tkinter import Grid
from turtle import filling, title
from matplotlib.style import use
import matplotlib.pyplot as plt
import pandas as pd
import PIL as pil
import os as o
from pytest import skip
import win32com.client as win32



    #  HOW TO READ CSV FILE
# filename = 'c:\\Python\\tst1.csv'
# df1 = pd.read_csv(filename)
# print(df1)
# print(o.getcwd())

    # HOW TO READ CSV FILE IN DATA FRAME
filename = 'C:\\Python\\data_s.csv'
df1 = pd.read_csv(filename)
    # HOW TO GET COLUMNS HEADER
# print(df1.columns)

    # DF HTML FORMAT
# df_11 = pd.read_csv(filename,skiprows=1,na_filter=False)

    # DF HTML FORMAT ( SERIES FRAME / SINGLE FRAME )
df_5 = pd.read_csv(filename,skiprows=1)
df_6 = pd.Series.to_frame(df_5.groupby(['hotelname'])['RNs'].sum()).reset_index()
df_6 = df_5.sort_values('RNs',ascending=True)
# df_5.to_html('c://python//html.html',index=False)

# print(df_5.head())

    # Sub Grouping
df_10 = df_6.groupby(['Month'])['bookings','RNs'].sum().reset_index()
# df_11 = df_10[['RNs']].sum().rename("Grand Total")  # For Grand Total
# df_12 = df_10.append(df_11).fillna('')  # Append Data Frame

print(df_10)

mypic = df_10.plot.bar(
    title="Rooms Night Trend",
    x = 'Month',
    figsize = (4,2),
    rot=0,
    stacked = False
).get_figure()
pic_save = 'c://Python//img1.jpg'
mypic.savefig(pic_save)

    # DF TO MAIL BODY IN TABLE FORMAT
# outlook = win32.Dispatch('Outlook.Application')
    # ''' ''' + df_10.to_html(index=False) + ''' <img src="'''+ pic_save +'''">  '''
    # + df_10.to_html(index=False) +

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





    #  HOW TO READ TOP 5 ROWS
# print(df1.head())

    # HOW TO READ BOTTOM 5 ROWS
# print(df1.tail())

    #  HOW TO USED COL AS PER REQ. 
# df1 = pd.read_csv(filename,usecols=[0])

    #  HOW TO GET COL INDEX NUMBER.
# print(df1.columns.get_loc('Bookings'.lower()))

    # SKIP ROWS IF HEADER NOT IN 1ST OR 1,2,3.. ROW USE IT.
# print(pd.read_csv(filename,skiprows=1))
# print(pd.read_csv(filename))

    # HOW TO CHG INDEX COLUMN
# print(pd.read_csv(filename,index_col='hotelname'))    # YOU CAN USED INDEX COL BY STRING OR INDEX COL NO.
# print(pd.read_csv(filename,index_col=2))  # YOU CAN USED INDEX COL BY STRING OR INDEX COL NO.

    # HOW TO GET HEADER OF 1/2 ROW NO. / ANY ROW AS PER REQ.
# print(pd.read_csv(filename, header=None))
# print(pd.read_csv(filename, header=1))

    # HOW TO CHG DATA TYPE AS PER OUR REQ.
# print(pd.read_csv(filename, skiprows=1, dtype={'hotelcode':'float64'}))

    # HOW TO BLACK CELL SHOW BLACK ( DEFAULT IT'S SHOWING NaN )
# print(pd.read_csv(filename, na_filter=False ))

    #  CHECK NULL VALUE ( IF NULL THE TRUE ELSE FALSE )
# print(pd.read_csv(filename ).isnull())
    
    # CHECK NOT NULL VALUE (IF NOT NULL THEN TRUE ELSE FALSE )
# print(pd.read_csv(filename ).notnull())

# print(pd.read_csv(filename, index_col=1))

    # COUNT NO. OF NULL VALUES IN DATAFRAME 
# print(pd.read_csv(filename, skiprows=1,na_filter=False).count())

