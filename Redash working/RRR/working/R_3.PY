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
Curr_month = int(date.today().strftime("%m"))

mapping_file = 'C:\\Python\\Redash working\\RRR\\File\\Mapping_Nov_.xlsx'
file_Travel = 'C:\\Python\\Redash working\\RRR\\File\\Travelled_Level_RN_Query_2_2022_11_17.csv'
file_Checkin = 'C:\\Python\\Redash working\\RRR\\File\\Checking_Level_RN_Query_3_2022_11_17.csv'
file_Book = 'C:\\Python\\Redash working\\RRR\\File\\Book_Level_RN_(India)_Query_1_2022_11_17.csv'
AP_LAST_MONTH = 'C:\\Python\\Redash working\\RRR\\File\\L_Month_AP_RNs_Growth_2022_11_17.csv'
AP_CURR_MONTH = 'C:\\Python\\Redash working\\RRR\\File\\C_Month_AP_RNs_Growth_2022_11_17.csv'
MASTER_REPO = 'C:\\Python\\Redash working\\RRR\\File\\Master Room Nights data repository.xlsb'
MEAL_PLAN = 'C:\\Python\\Redash working\\RRR\\File\\MealPlan-RNs_Vin_2022_11_17.csv'

df_map_main = pd.read_excel(mapping_file,sheet_name='Data')
df_map_ind = df_map_main.loc[(df_map_main['Team'].isin(['NICE','SWAG']))]
# df_Travel = pd.read_csv(file_Travel)
df_checkin = pd.read_csv(file_Checkin)
df_Book = pd.read_csv(file_Book)
# df_AP_L_MONTH = pd.read_csv(AP_LAST_MONTH)
# f_AP_C_MONTH = pd.read_csv(AP_CURR_MONTH)
# df_meal_plan = pd.read_csv(MEAL_PLAN)

bdm_list = df_map_ind['BDM Name'].unique()

def notepad_working():
    notepad_file = "c:\\Python\\Redash working\\rrr\\bdm_name.txt"
    with open(notepad_file,"a+") as f:
        for x in range(len(bdm_list)):  f.write(f"\n{bdm_list[x]}\t\t\t{len(df_map_ind[df_map_ind['BDM Name']== bdm_list[x]])}")

def bdm_h_map(bd_name):
    bdm_hotel_list = len(df_map_ind[df_map_ind['BDM Name']== bd_name])
    return bdm_hotel_list

def Book_rn_curr_last(bd_name):
    print(bd_name)
    df_book_rns = pd.merge(left=df_Book,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='left')
    df_book_rns_c = df_book_rns.loc[(df_book_rns['Booking_Month'] == Curr_month ) & (df_book_rns['BDM Name'] == bd_name )]
    print("Current Month Book Total Hotels RNs :-  ", df_book_rns_c['RNs'].sum())
    print(f"Current Month Total {bdm_h_map(bd_name)} RNs {df_book_rns_c['RNs'].sum()} Percentage {(df_book_rns_c['RNs'].sum()/bdm_h_map(bd_name)).round(2)}%")
    # Last Month RNs
    df_book_rns_l = df_book_rns.loc[(df_book_rns['Booking_Month'] == lst_month) & (df_book_rns['BDM Name'] == bd_name)]
    print("Last Month Book Total Hotels RNs :-  ", df_book_rns_l['RNs'].sum())
    print(f"Last Month Total {bdm_h_map(bd_name)}  RNs {df_book_rns_l['RNs'].sum()} Percentage {(df_book_rns_l['RNs'].sum()/bdm_h_map(bd_name)).round(2)}%")
# Booked_level_Output
    Final_Book = "not complete / working"

def checkin_level(bd_name):
    print("Checkin Level","")
    df_checkin['Booking_Date'] = pd.to_datetime(df_checkin['Booking_Date'])
    df_days = df_checkin.loc[(df_checkin['Booking_Date']>= today_minus_5) & (df_checkin['Booking_Date']<= today_plus_5)]
    df_bdm = pd.merge(left=df_map_ind,right=df_days,left_on="Hotelcode",right_on="hotelcode",how="left")
    df_bdm.columns = df_bdm.columns.str.replace(' ','_')
    df_bdm =df_bdm[['Hotelcode','Hotel_Name','Activation_Status','RM_Name','ZM_Name','BDM_Name','KAM_Name','Team','hotelcode','Booking_Date','bookings','RNs','GMV']]
    df_bdm = df_bdm[df_bdm['BDM_Name'] == bd_name]
    df_bdm = df_bdm[['hotelcode','BDM_Name','Booking_Date','RNs','GMV']]
    df_bdm['Booking_Date'] = pd.to_datetime(df_bdm['Booking_Date']).dt.date
    df_bdm2 = pd.pivot_table(df_bdm,index=['BDM_Name'],columns='Booking_Date',values='RNs',aggfunc='sum').reset_index()
    df_bdm2['TYPE'] = 'RNS'    
    df_bdm3 = df_bdm.pivot_table(index='BDM_Name',columns='Booking_Date',values='GMV',aggfunc='sum').reset_index()
    df_bdm3['TYPE'] = 'GMV'    
    df_bdm4 = df_bdm2.append(df_bdm3)
    first = df_bdm4.pop('TYPE')
    df_bdm4.insert(0,'Type',first)
    df_bdm4.to_csv("c:\\Python\\Redash working\\RRR\\bdm_output_rn_gmv.csv",index=False)
    df_bdm4.to_html('c:\\Python\\Redash working\\RRR\\bdm_output_rn_gmv.html',index=False)

def asp_formula(hotelcode,gmv,rn):
    val = int(gmv)/int(rn)    
    list = []
    if (val>0 and val<2000): list.append([hotelcode,"0-2K"])
    elif (val>=2000 and val<4000): list.append([hotelcode,"2-4K"])
    elif (val>=4000 and val<6000): list.append([hotelcode,"4-6K"])
    elif (val>=6000): list.append([hotelcode,"6 K+"])
#     elif (val='NA'): list.append([hotelcode,'NA'])
    else: list.append([hotelcode,"NA"])
    return list

# asp_formula(1001,10,10)

def asp(bd_name):
    print("Asp")
    df_book_rns = pd.merge(left=df_Book,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='inner')

    
    
    # df_book_rns_c = df_book_rns.loc[(df_book_rns['Booking_Month'] == Curr_month ) & (df_book_rns['BDM Name'] == bd_name )]
    # print("Current Month Book Total Hotels RNs :-  ", df_book_rns_c['RNs'].sum())
    # print(f"Current Month Total {bdm_h_map(bd_name)} RNs {df_book_rns_c['RNs'].sum()} Percentage {(df_book_rns_c['RNs'].sum()/bdm_h_map(bd_name)).round(2)}%")
    # # Last Month RNs
    # df_book_rns_l = df_book_rns.loc[(df_book_rns['Booking_Month'] == lst_month) & (df_book_rns['BDM Name'] == bd_name)]
    # print("Last Month Book Total Hotels RNs :-  ", df_book_rns_l['RNs'].sum())
    # print(f"Last Month Total {bdm_h_map(bd_name)}  RNs {df_book_rns_l['RNs'].sum()} Percentage {(df_book_rns_l['RNs'].sum()/bdm_h_map(bd_name)).round(2)}%")






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