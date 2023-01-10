# imports for SQL data part
import pyodbc as odbc
import pandas as pd
from datetime import datetime

date = datetime.today()

driver_name = 'SQL SERVER'
SERVER_NAME = "VINEET-PC\SQLEXPRESS"
DATABSE_NAME = "hotel"
#  Type 1 for connection 
# connect with sql server
# connect_string = f"""
#     DRIVER={{{driver_name}}};
#     SERVER={SERVER_NAME};
#     DATABASE={DATABSE_NAME};
#     Trust_Connection=yes;
# """
# conn = odbc.connect(connect_string)

# Type 2 for connection
conn = odbc.connect('Driver={SQL SERVER};' 'Server=VINEET-PC\SQLEXPRESS;' 'Database=hotel;' 'Trust_Connection=yes;')
cursor = conn.cursor()

filepath = r"C:\Users\Owner\Desktop\testing heavy data\hotels\hotel list.xlsx"
df1 = pd.read_excel(filepath,sheet_name='Sheet1',index_col=False)
df1['date'] = pd.to_datetime(df1['date'],format='%d/%m/%y')
df1['hotelname'] = df1['hotelname'].astype(str)

def list_append():
    l2 = []
    for i in range(0,4):
        a = df1.iloc[i][0].strftime("%d/%m/%y")
        b = df1.iloc[i][1].astype(str)
        c = df1.iloc[i][2]
        l2.append((a,b,c))
    # for i in l2:
    #     print(i)
    #     cursor.execute('INSERT INTO [hotel].[dbo].[Table_2] VALUES(?,?,?);',(i))
    #     conn.commit()
    
def Read(T_Name):
    print("Read")
    cursor = conn.cursor()
    cursor.execute(f"Select * from {T_Name}")
    for x in cursor:
        print(x)
    cursor.close()
# Read('[hotel].[dbo].[Table_2]') # For Checking

def Write(Tablename, date,hotelcode,hotelname):
    print("Write")
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {Tablename} VALUES (?,?,?);',(date,hotelcode,hotelname))
    cursor.commit()
    cursor.close()
# Write('[hotel].[dbo].[Table_2]','10/1/2023','1004','hotel_1004')


def Detele(Tablename,HOTELCODE,CONDITION):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {Tablename} WHERE {HOTELCODE} = {CONDITION};')
    cursor.commit()
    print(f'{HOTELCODE} : {CONDITION} Was Deleted')
    cursor.close() 
# Detele('[hotel].[dbo].[Table_2]','hotelcode','1003')  # For Delete


def Update(T_Name,col_name,new_val,condition_col_name,condition_val):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {T_Name} SET {col_name} = '{new_val}' where {condition_col_name} = {condition_val} ")
    cursor.commit()
    # print(f"Record Was Updated old value \t{row_val} :\t new value {new_val}")
    cursor.close()
# Update('[hotel].[dbo].[Table_2]','hotelname',"hotel_1031",'hotelcode','1000011031')   # For Update


Read('[hotel].[dbo].[Table_2]') # For Checking
conn.close()