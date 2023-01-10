from tkinter import font
import pandas as pd
from datetime import datetime as dt
import datetime, time
from datetime import timedelta
from datetime import date
from datetime import datetime
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import seaborn as sns
import win32com.client as win32

st = datetime.utcnow()
c_date = datetime.now().strftime("%Y_%m_%d_%I_%M_%p")

print("today ",c_date)
today_minus_5 = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
today_plus_5 = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
lst_month = int(date.today().strftime("%m"))-1

# file_Checkin = 'C:\\Python\\Redash working\\RRR\\File\\Checking_Level_(India)_RN_Query_3_2022_11_09.csv'
file_Book = 'C:\\Python\\Redash working\\RRR\\File\\Book_Level_RN_(India)_Query_1_2022_11_09.csv'
# file_Travel = 'C:\\Python\\Redash working\\RRR\\File\\Travelled_Level_RN_(India)_Query_2_2022_11_09.csv'
mapping_file = 'C:\\Python\\Redash working\\RRR\\File\\Mapping_Nov_.xlsx'

df_Book = pd.read_csv(file_Book)
# df_Travel = pd.read_csv(file_Travel)
# df_checkin = pd.read_csv(file_Checkin)
df_map_main = pd.read_excel(mapping_file,sheet_name='Data')
df_map_ind = df_map_main.loc[(df_map_main['Team'].isin(['NICE','SWAG']))]

bdm_list = df_map_ind['BDM Name'].unique()

# with open("c:\\Python\\Redash working\\rrr\\bdm_name.txt","a+") as f:
#     for x in range(len(bdm_list)):  f.write(f"\n{bdm_list[x]}\t\t\t{len(df_map_ind[df_map_ind['BDM Name']== bdm_list[x]])}")

# DONE 
# Booking level
bdm_hotel_list = len(df_map_ind[df_map_ind['BDM Name']== "Aanchal Khewal"])
print("Total Hotels :-  ",bdm_hotel_list)
# Current Month RNs
df_book_rns = df_Book.loc[(df_Book['Booking_Month'] == 11) & (df_Book['bdm_name_info'] == "Aanchal Khewal" )]
print("Current Month Book Total Hotels RNs :-  ", df_book_rns['RNs'].sum())
print(f"Current Month Total {bdm_hotel_list}  RNs {df_book_rns['RNs'].sum()} Percentage {(df_book_rns['RNs'].sum()/bdm_hotel_list).round(2)}%")

# Last Month RNs
df_book_rns = df_Book.loc[(df_Book['Booking_Month'] == 10) & (df_Book['bdm_name_info'] == "Aanchal Khewal" )]
print("Last Month Book Total Hotels RNs :-  ", df_book_rns['RNs'].sum())
print(f"Last Month Total {bdm_hotel_list}  RNs {df_book_rns['RNs'].sum()} Percentage {(df_book_rns['RNs'].sum()/bdm_hotel_list).round(2)}%")


# DONE # checkin level
# df_checkin['Booking_Date'] = pd.to_datetime(df_checkin['Booking_Date'])
# df_days = df_checkin.loc[(df_checkin['Booking_Date']>= today_minus_5) & (df_checkin['Booking_Date']<= today_plus_5)]
# df_bdm = pd.merge(left=df_map_ind,right=df_days,left_on="Hotelcode",right_on="hotelcode",how="left")
# df_bdm.columns = df_bdm.columns.str.replace(' ','_')
# df_bdm =df_bdm[['Hotelcode','Hotel_Name','Activation_Status','RM_Name','ZM_Name','BDM_Name','KAM_Name','Team','hotelcode','Booking_Date','bookings','RNs','GMV']]
# df_bdm.to_csv("c:\\Python\\Redash working\\RRR\\merge_output.csv",index=False)
# df_bdm = df_bdm[['hotelcode','BDM_Name','Booking_Date','RNs']]
# df_bdm.to_csv("c:\\Python\\Redash working\\RRR\\bdm_output_checkin.csv",index=False)
# df_bdm2 = df_bdm.pivot_table(index='BDM_Name',columns='Booking_Date',values='RNs',aggfunc='sum').reset_index()
# df_bdm2.to_csv("c:\\Python\\Redash working\\RRR\\bdm_output_checkin.csv",index=False)



# df_Book = df_Book.loc[(df_Book['Booking_Month'] >=10)]




# df.groupby(['Team']).agg({"Rank":['count','sum'],'Year':['min','max']})) # working

# df_days = df_days.pivot_table(index='hotelcode',columns='Booking_Date').head(100).reset_index().fillna("").to_html(table_id='my_id',index=False,)
# df_days_html = df_days.replace('class="dataframe" id="my_id">','class="styled-table" id="my_id">')

# with open('C:\\Users\\mmt9642\\Desktop\\pankaj\\style.txt') as style_file:
#     html_style_table = style_file.read()
# final_html = html_style_table + df_days_html
# with open("c:\\Python\\Redash working\\RRR\\days2.html", "w") as html_file:
#     html_file.write(final_html)


# # with pd.ExcelWriter('c:\output.xlsx') as writer:  
# #     df.to_excel(writer, sheet_name='Sheet_name_1')    

# unique_regional_head = []
# for i in df.regional_head.unique(): unique_regional_head.append(i)

# for i in range(0,1):
#     group = df.groupby(['regional_head','day'])['RNs'].sum().to_frame().reset_index()
#     group_ = group.pivot_table(index='regional_head',columns='day').reset_index()
    
#     # group_ = df.query("regional_head =='{rm}'".format(rm = unique_regional_head[i]))
#     # group_ = group_.groupby(['regional_head','day'])['RNs'].sum().to_frame().reset_index()
#     html_table = group_.to_html(table_id='my_id',index=False)
#     html_table = html_table.replace('class="dataframe" id="my_id">','class="styled-table" id="my_id">')
    
#     with open('C:\\Users\\mmt9642\\Desktop\\pankaj\\style.txt') as style_file:
#         html_style_table = style_file.read()
    
#     body_html = '''
#     <p style="color:blue;font-size:14px;text-align:left;">
#     Hi '''+unique_regional_head[i].title()+''', <br/><br/>

#     This is Test Mail on:  <b>'''+ c_date + ''' </b><br/> </p> 
#     '''    
#     gap = '''<br>'''

#     # used for :- Outside body file for dynamic code
#     # with open('c:\\Users\\mmt9642\\Desktop\\pankaj\\body.txt') as body_file:
#     #     body_html = body_file.read()

#     final_html = html_style_table + body_html + gap + gap + html_table

#     with open("C:\\Users\\mmt9642\\Desktop\\pankaj\\RM_Base__html_file.html", "w") as html_file:
#         html_file.write(final_html)
#         print(final_html)

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

ed = datetime.utcnow()
print("complete  ",(ed - st))