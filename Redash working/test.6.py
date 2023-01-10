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
from datetime import timedelta

# c_date = datetime.now().strftime("%Y_%m_%d")
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")
file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\RNs_data#Recovery_growth_-_CheckIn_-Vin_2022_11_05 .csv'
mapping_file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\Mapping.xlsx'
df1 = pd.read_csv(file)
df2 = pd.read_excel(mapping_file,sheet_name='Data')

today = pd.to_datetime(pd.Timestamp.now().strftime('%d-%m-%Y'),format="%d-%m-%Y")

# df1 filter
df1['Booking_Date'] = pd.to_datetime(df1['Booking_Date'],format="%d-%m-%Y")
df1['day'] = df1['Booking_Date'].dt.day
max = df1['Booking_Date'].max()
df1 = df1[df1['Booking_Date']> max-timedelta(5)]    # timedelta for 5 days gap

# # check no of days diff.
# print(today-max)    
# if "1 days" in str(today-max):  
#     print("yes")
#     a = "run"
# else:   
#     print("no")
#     a = "stop"
# # For Code terminate
# if a == "stop": quit()

# df2 filter
df2 = df2[df2['TEAM'].isin(['NICE','SWAG'])]

# merge
df = pd.merge(left=df1,right=df2,left_on='hotelcode',right_on="Hotelcode",how="left")

unique_rm = []
for i in df['RM Name'].unique(): unique_rm.append(i)
print(unique_rm)

df_rm = df.groupby(['RM Name','day'],as_index=True)['RNs'].sum().to_frame().reset_index()
print(df_rm.head(10))
rm_group = df_rm.pivot_table(index='RM Name',columns='day').reset_index()
print(rm_group.head(10))
rm_html = rm_group.to_html(table_id='my_id',index=False)
df_city = df.groupby(["city",'day'],as_index=True)["RNs"].sum().to_frame().reset_index().sort_values('RNs',ascending=False)
top_10_city = df_city.pivot_table(index="city",columns='day').reset_index().head(10)
print(top_10_city.head(10))
city_html = top_10_city.to_html(table_id='my_id',index=False)

rm_html_t1 = rm_html.replace('class="dataframe" id="my_id">','class="styled-table" id="my_id">')
city_html_t2 = city_html.replace('class="dataframe" id="my_id">','class="styled-table" id="my_id">')
    
with open('C:\\Users\\mmt9642\\Desktop\\pankaj\\style.txt') as style_file:
    html_style_table = style_file.read()
    
#     body_html = '''
#     <p style="color:blue;font-size:14px;text-align:left;">
#     Hi '''+unique_regional_head[i].title()+''', <br/><br/>

#     This is Test Mail on:  <b>'''+ c_date + ''' </b><br/> </p> 
#     '''    
#     gap = '''<br>'''

#     # used for :- Outside body file for dynamic code
#     # with open('c:\\Users\\mmt9642\\Desktop\\pankaj\\body.txt') as body_file:
#     #     body_html = body_file.read()

final_html_1 = html_style_table + rm_html_t1
final_html_2 = html_style_table + city_html_t2

with open("C:\\Users\\mmt9642\\Desktop\\pankaj\\RM_html_.html", "w") as html_file_1:
    html_file_1.write(final_html_1)
    print(final_html_1)

with open("C:\\Users\\mmt9642\\Desktop\\pankaj\\City_html_.html", "w") as html_file_2:
    html_file_2.write(final_html_2)
    print(final_html_2)

#     # # DF TO MAIL BODY IN TABLE FORMAT
#     # outlook = win32.Dispatch('Outlook.Application')
#     # mail = outlook.CreateItem(0)
#     # mail.Subject = "This subject line"
#     # mail.To = 'vineet.verma@go-mmt.com'
#     # mail.HTMLBody = final_html
#     # mail.Display()
#     # # mail.Send()

#     # group_ = df.query("regional_head =='{rm}'".format(rm = unique_regional_head[i])).groupby(['regional_head','day'])['RNs'].sum()
#     #  pic = group_.plot(kind='bar',xlabel="No's of Days",ylabel='Room Night',title = unique_regional_head[i].upper()).get_figure()    
#     #  pic.savefig('c:\\Python\\img_0'+str([i]))
#     #  plt.show()
#     #  plt.clf()
#     # print(group_)
#     #  pic2 = sns.lineplot('RNs')
#     #  sns.show()