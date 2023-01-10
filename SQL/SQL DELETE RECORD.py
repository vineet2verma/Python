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

# DELETE SINGLE RECORD
query = "DELETE FROM classes WHERE s_no='4' "
cursor.execute(query)
conn.commit()
conn.close()

print("done")

