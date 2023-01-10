# https://redash.goibibo.com/queries/41894/source?p_Start%20Date=2022-06-01&p_End%20Date=2022-06-30 # Pankaj Query

from unittest import skip
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import jinja2

file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\RNs_data#Recovery_growth_-_CheckIn_2022_10_29 (2).csv'
mapping_file = 'C:\\Users\\mmt9642\\Desktop\\pankaj\\Mapping for operational flow_Oct-22.xlsx'
df1 = pd.read_csv(file)
df2 = pd.read_excel(mapping_file,sheet_name='Data')
df = pd.merge(left=df1,right=df2,left_on='hotelcode',right_on="Hotelcode",how="left")

df['Booking_Date'] = pd.to_datetime(df['Booking_Date'])
df['day'] = df.Booking_Date.dt.day
df = df.loc[(df['Booking_Date'] > "2022-06-25") & (df['Booking_Date'] <= "2022-06-30")]
df.columns = df.columns.str.replace(' ','_')

unique_rm = []
for i in df.RM_Name.unique(): unique_rm.append(i)

# Grouping 
group = df.groupby(['RM_Name','day'])['RNs'].sum().reset_index()
group = group.style.highlight_max(axis=0)
print(group)

# Pivot 
pivot = group.pivot_table(index=['RM_Name'],columns=['day'],aggfunc=['sum'])
pivot = pivot.style.highlight_max(axis=0)
print(pivot)

#Create a writer-object   
with pd.ExcelWriter('output.xlsx') as writer:  
    pivot.to_excel(writer, sheet_name='Sheet_name_1')

df = pd.read_excel('c:\\Python\\output.xlsx',skiprows=2)

# Remove Row as per index no. & Rename it.
df = df.rename(columns={"day":"RM_Name"}).drop(0)
df.style.highlight_max(axis=0)
print(df)



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





