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
c_day = int(date.today().strftime("%d"))
lm_day = int((date.today()-timedelta(days=c_day)).strftime("%d"))

mapping_file = 'C:\\Python\\Redash working\\RRR\\File\\Mapping_Nov_.xlsx'
file_Travel = 'C:\\Python\\Redash working\\RRR\\File\\Travelled_Level_RN_Query_2_2022_11_17.csv'
file_Checkin = 'C:\\Python\\Redash working\\RRR\\File\\Checking_Level_RN_Query_3_2022_11_17.csv'
file_Book = 'C:\\Python\\Redash working\\RRR\\File\\Book_Level_RN_(India)_Query_1_2022_11_17.csv'
AP_LAST_MONTH = 'C:\\Python\\Redash working\\RRR\\File\\L_Month_AP_RNs_Growth_2022_11_17.csv'
AP_CURR_MONTH = 'C:\\Python\\Redash working\\RRR\\File\\C_Month_AP_RNs_Growth_2022_11_17.csv'
MEAL_PLAN = 'C:\\Python\\Redash working\\RRR\\File\\MealPlan-RNs_Vin_2022_11_17.csv'
MAST_RN_NOV = 'C:\\Python\\Redash working\\RRR\\File\\RNs_Repo_Nov.csv'
MAST_RN_DEC = 'C:\\Python\\Redash working\\RRR\\File\\RNs_Repo_Dec.csv'

df_map_main = pd.read_excel(mapping_file,sheet_name='Data')
df_map_ind = df_map_main.loc[(df_map_main['Team'].isin(['NICE','SWAG']))]

df_checkin = pd.read_csv(file_Checkin)
df_Book = pd.read_csv(file_Book)
df_meal_plan = pd.read_csv(MEAL_PLAN)

df_AP_L_MONTH = pd.read_csv(AP_LAST_MONTH)
df_AP_C_MONTH = pd.read_csv(AP_CURR_MONTH)

df_Book_Nov2019 = pd.read_csv(MAST_RN_NOV)
df_Book_Dec2019 = pd.read_csv(MAST_RN_DEC)
df_2019_1 = [df_Book_Nov2019,df_Book_Dec2019]
df_2019_2 = pd.concat(df_2019_1)

bdm_list = df_map_ind['BDM Name'].unique()

def merge(*li):
        co = []
        for aa in [li]:
            for bb in aa:   co = co + bb
        return co

def bdm_h_map(bd_name):
    bdm_hotel_list = len(df_map_ind[df_map_ind['BDM Name']== bd_name])
    return bdm_hotel_list

def Book_rn_curr_last(bd_name):
    print("1 ",bd_name)
    df_book_rns = pd.merge(left=df_Book,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='left')
    df_book_rns_c = df_book_rns.loc[(df_book_rns['Booking_Month'] == Curr_month ) & (df_book_rns['BDM Name'] == bd_name )]  
    df_book_rns_l = df_book_rns.loc[(df_book_rns['Booking_Month'] == lst_month) & (df_book_rns['BDM Name'] == bd_name)]
    df_book_2019_3 = pd.merge(left=df_2019_2,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='left')
    df_book_2019 = df_book_2019_3.loc[(df_book_2019_3['Booking_Month'] == Curr_month) & (df_book_2019_3['BDM Name'] == bd_name)]
    
    def book_data_func(bd_name,dframe):
        bdm_name = bd_name
        bdm_hmap = bdm_h_map(bdm_name)
        Year = dframe['Booking_Year'].max()
        Month = dframe['Booking_Month'].max()
        Sold = dframe['RNs'].sum()
        Dispersion = (Sold/bdm_hmap).round()
        book_data = [{'Name' : bdm_name,'Total_hotels' : bdm_hmap, 'Year' : Year, 'Month' : Month, 'RNs' : Sold,'Dispersion %': Dispersion }]
        return book_data
    l11 = merge(book_data_func(bd_name,df_book_rns_c) , book_data_func(bd_name,df_book_rns_l),book_data_func(bd_name,df_book_2019))
    book_df11 = pd.DataFrame(l11)
    book_df11.to_html('c:\\Python\\Redash working\\RRR\\'+bd_name+'_one.html',index=False)
    
def checkin_level(bd_name):
    print("2 ",bd_name)
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
    first = df_bdm2.pop('TYPE')
    df_bdm2.insert(0,'Type',first)
    df_bdm2.to_html('c:\\Python\\Redash working\\RRR\\'+bd_name+'two.html',index=False)

def asp(bd_name):
    print("3 ",bd_name)
    df_book_rns = pd.merge(left=df_Book,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='inner')
    df_book_rns = df_book_rns.loc[(df_book_rns['BDM Name'] == bd_name )]
    df_book_2019_3 = pd.merge(left=df_2019_2,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='left')
    df_book_2019 = df_book_2019_3.loc[(df_book_2019_3['Booking_Month'] == Curr_month) & (df_book_2019_3['BDM Name'] == bd_name)]
    df_book_3 = pd.concat([df_book_rns,df_book_2019])
    df_book_3 = df_book_3[['ASP bucket','Booking_Year','Booking_Month']]
    df_book_30 = df_book_3.groupby(['ASP bucket','Booking_Year','Booking_Month'])['ASP bucket'].count().rename('Count').reset_index()
    bf_book_4 = df_book_30.pivot_table(index=['ASP bucket'],columns=['Booking_Year','Booking_Month'],values='Count')
    bf_book_4['Growth'] = ((bf_book_4[2022][11]/bf_book_4[2019][11]).round(2)).astype(float)
    bf_book_4.to_html('c:\\Python\\Redash working\\RRR\\'+bd_name+'three.html',index=False)

def hl_rn_view(bd_name):
    print("4 ",bd_name)
    hl1 = pd.merge(left=df_Book,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='left')
    hl2 = hl1.loc[(hl1['BDM Name']==bd_name)]
    hl3 = hl2[['BDM Name','hotelcode','Hyper Location- Category','Booking_Year','Booking_Month','bookings','RNs','GMV']]
    hl4 = (hl3.groupby(['Hyper Location- Category'])['RNs'].sum().reset_index()).sort_values(by='RNs',ascending=False)
    hl4.head(3).to_html('c:\\Python\\Redash working\\RRR\\'+bd_name+'four_top.html',index=False)
    
def meal_plan(bd_name):
    print("5 ",bd_name)
    meal_plan1 = pd.merge(left=df_meal_plan,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='left')
    meal_plan_c = meal_plan1.loc[(meal_plan1['Booking_Month'] == Curr_month ) & (meal_plan1['BDM Name'] == bd_name )]
    meal_plan_l = meal_plan1.loc[(meal_plan1['Booking_Month'] == lst_month ) & (meal_plan1['BDM Name'] == bd_name )]
    meal_plan_c['RN/DAYS'] = (meal_plan_c['RNs']/c_day)
    meal_plan_l['RN/DAYS'] = (meal_plan_l['RNs']/lm_day)
    group_c = meal_plan_c.groupby(['Booking_Year','Booking_Month','mealplan'])['RN/DAYS'].sum().round(2).reset_index()    
    group_l = meal_plan_l.groupby(['Booking_Year','Booking_Month','mealplan'])['RN/DAYS'].sum().round(2).reset_index()
    df10 = pd.concat([group_c,group_l])
    df10['mealplan'] = df10['mealplan'].replace('SMAP','Other')
    df11 = df10.pivot(index=['mealplan'],columns=['Booking_Year','Booking_Month'])
    pd.options.mode.chained_assignment = None
    df11.to_html('c:\\Python\\Redash working\\RRR\\'+bd_name+'five.html')

def ap_window(bd_name):
    print("6 ", bd_name)
    df_ap = [df_AP_C_MONTH,df_AP_L_MONTH]
    df_ap1 = pd.concat(df_ap)
    df_ap2 = pd.merge(left=df_ap1,right=df_map_ind,left_on='hotelcode',right_on='Hotelcode',how='left')
    df_ap3 = df_ap2.loc[(df_ap2['BDM Name'] == bd_name )]
    df_ap4 = df_ap3.groupby(['AP_window','Booking_Year','Booking_Month'])['RNs'].sum().reset_index()
    df_ap5 = df_ap4.pivot(index=['AP_window'],columns=['Booking_Year','Booking_Month'],values=['RNs']).reset_index().rename_axis("S.No",axis=0)
    df_ap5.to_html('c:\\Python\\Redash working\\RRR\\'+bd_name+'six.html')


ed = datetime.utcnow()
print("complete  ",(ed - st))

for i in range(3):
    bd_name = bdm_list[i]
    print(bd_name,bdm_h_map(bd_name))
    Book_rn_curr_last(bd_name)
    checkin_level(bd_name)
    asp(bd_name)
    hl_rn_view(bd_name)
    meal_plan(bd_name)
    ap_window(bd_name)



