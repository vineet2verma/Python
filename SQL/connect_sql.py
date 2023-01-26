import sys
import pypyodbc as odbc
import pandas as pd

DRIVERS = 'SQL Server'
SERVER_NAME = 'VINEET-PC\SQLEXPRESS'
DATABASE_NAME = "school"

# 1st Way to connection
conn_string = f"""
DRIVER= {{{DRIVERS}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;
"""

# 2nd Way to Connection
# conn_string = (
#     r'DRIVER={SQL Server};'
#     r'SERVER=VINEET-PC\SQLEXPRESS;'
#     r'DATABASE=school;'
#     r'Trusted_Connection=yes;'
#     )

try:
    conn = odbc.connect(conn_string)
except Exception as e:
    print(e)
    print("Task is Terminated")
    sys.exit()
else:
    cursor = conn.cursor()

sql_query = """
    select * from classes
"""

# # Read sql Data with Header
df1 = pd.read_sql(sql_query, conn)
print(df1)

# Read Sql Data without Header
# c = conn.cursor()
# data  = c.execute(sql_query)
# df2 = pd.DataFrame(data)
# print(df2)

# Statement Run
# insert_statement = """
#     INSERT INTO classes
#     values (?,?,?)
# """

# records = [
#     [2,'two','two_other'],[3,'three','three_other']
# ]


# try:
#     for record in records:
#         print(record)
#         cursor.execute(insert_statement,record)
# except Exception as e:
#     cursor.rollback()
#     print(e.value)
#     print('transaction roll back')
# else:
#     print('records successfully inserted')
#     cursor.commit()
# finally:
#     if conn.connected == 1:
#         print('Connection Close')
#         conn.close()