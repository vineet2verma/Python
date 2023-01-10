# https://redash.goibibo.com/queries/41894/source?p_Start%20Date=2022-06-01&p_End%20Date=2022-06-30
# https://redash.goibibo.com/queries/47538/source  ( Room Night Query)

from tkinter import font
import pandas as pd
from datetime import datetime as dt
import datetime
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import seaborn as sns
import win32com.client as win32

# c_date = datetime.now().strftime("%Y_%m_%d")
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\RNs_data#Recovery_growth_-_CheckIn_2022_10_29 (2).csv'
mapping_file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\Mapping.xlsx'
df = pd.read_csv(file)
df2 = pd.read_excel(mapping_file,sheet_name='Data')
# print(df2.head())

df['Booking_Date'] = pd.to_datetime(df['Booking_Date'])
df = df.sort_values(by='Booking_Date')
df['day'] = df.Booking_Date.dt.day

df = df.loc[
    (df['Booking_Date'] > "2022-06-25") & 
    (df['Booking_Date'] <= "2022-06-30")]

# with pd.ExcelWriter('c:\output.xlsx') as writer:  
#     df.to_excel(writer, sheet_name='Sheet_name_1')    

unique_regional_head = []
for i in df.regional_head.unique(): unique_regional_head.append(i)

for i in range(0,1):
    group = df.groupby(['regional_head','day'])['RNs'].sum().to_frame().reset_index()
    group_ = group.pivot_table(index='regional_head',columns='day').reset_index()
    
    # group_ = df.query("regional_head =='{rm}'".format(rm = unique_regional_head[i]))
    # group_ = group_.groupby(['regional_head','day'])['RNs'].sum().to_frame().reset_index()
    html_table = group_.to_html(table_id='my_id',index=False)
    html_table = html_table.replace('class="dataframe" id="my_id">','class="styled-table" id="my_id">')
    
    with open('C:\\Users\\mmt9642\\Desktop\\pankaj\\style.txt') as style_file:
        html_style_table = style_file.read()
    
    body_html = '''
    <p style="color:blue;font-size:14px;text-align:left;">
    Hi '''+unique_regional_head[i].title()+''', <br/><br/>

    This is Test Mail on:  <b>'''+ c_date + ''' </b><br/> </p> 
    '''    
    gap = '''<br>'''

    # used for :- Outside body file for dynamic code
    # with open('c:\\Users\\mmt9642\\Desktop\\pankaj\\body.txt') as body_file:
    #     body_html = body_file.read()

    final_html = html_style_table + body_html + gap + gap + html_table

    with open("C:\\Users\\mmt9642\\Desktop\\pankaj\\RM_Base__html_file.html", "w") as html_file:
        html_file.write(final_html)
        print(final_html)

    # # DF TO MAIL BODY IN TABLE FORMAT
    # outlook = win32.Dispatch('Outlook.Application')
    # mail = outlook.CreateItem(0)
    # mail.Subject = "This subject line"
    # mail.To = 'vineet.verma@go-mmt.com'
    # mail.HTMLBody = final_html
    # mail.Display()
    # # mail.Send()

    # group_ = df.query("regional_head =='{rm}'".format(rm = unique_regional_head[i])).groupby(['regional_head','day'])['RNs'].sum()
    #  pic = group_.plot(kind='bar',xlabel="No's of Days",ylabel='Room Night',title = unique_regional_head[i].upper()).get_figure()    
    #  pic.savefig('c:\\Python\\img_0'+str([i]))
    #  plt.show()
    #  plt.clf()
    # print(group_)
    #  pic2 = sns.lineplot('RNs')
    #  sns.show()