# imports for SQL data part
import pyodbc as odbc
import pandas as pd

#  Type 1 for connection 
# driver_name = 'SQL SERVER'
# SERVER_NAME = "VINEET-PC\SQLEXPRESS"
# DATABSE_NAME = "school"
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

# Sql Read Function
def Read(Table_Name):
    cursor = conn.cursor()
    print('Read')
    cursor.execute(f"Select * from {Table_Name}")
    for row in cursor:
        print(row)
    cursor.commit()
    cursor.close()
Read('Table_2')

# Simple Method for Extract Records
# query = "SELECT * FROM Table_2"
# record = cursor.execute(query)

#  Extract all Record in Data Frame
# query = "SELECT * FROM Table_2"
# df1 =pd.read_sql_query(query,conn)          # Read SQL Query
# df1 = pd.read_sql(sql=query,con=conn)     # Read SQL Query
# print(len(df1))
# print("done")
