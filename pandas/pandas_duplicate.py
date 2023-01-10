# REMOVE DUPLICATE
from asyncore import read
import pandas as pd
from pandas import read_excel, merge

wb1 = "C:\CHKING\INDEX_MATCH\MASTER.xlsx"
wb2 = "C:\CHKING\INDEX_MATCH\HOTEL_NAME.xlsx"

df1 = read_excel(wb1,sheet_name="ID")
print(df1)
df2 =  df1.drop_duplicates()

print(df2)
