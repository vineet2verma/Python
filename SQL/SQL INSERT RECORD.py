# imports for SQL data part
import pyodbc as odbc
import pandas as pd

driver_name = 'SQL SERVER'
SERVER_NAME = "VINEET-PC\SQLEXPRESS"
DATABSE_NAME = "school"

# connect with sql server
connect_string = f"""
    DRIVER={{{driver_name}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABSE_NAME};
    Trust_Connection=yes;
"""
conn = odbc.connect(connect_string)
cursor = conn.cursor()

# INSERT SINGLE RECORD
# query = "INSERT INTO classes VALUES (9,'NINE','NINE@GMAIL.COM')"
# cursor.execute(query)
# conn.commit()

# INSERT CLAUSE FOR MULTIPLE INSERT RECORD 
# insert_into = """
#     INSERT INTO classes
#     VALUES (?,?,?)
# """


# LIST1 = [(5,'FIVE','FIVE@GMAIL.COM'),(6,'SIX','SIX@GMAIL.COM'),(7,'SEVEN','SEVEN@GMAIL.COM'),(8,'EIGHT','EIGHT@GMAIL.COM')]
# for x in LIST1:
#     cursor.execute(insert_into,x)
#     conn.commit()
# conn.closed()
# print("done")

