from operator import index
from numpy import inner
import openpyxl
import pandas as pd
import xlwings as xw

neo_file = 'C:\\Reporting\\Neo Chains\\Files\\Neo_Chain_2022_07_22_09_40_AM.csv'
mapping = 'C:\\Reporting\\Neo Chains\\Neo Chain -testing_.xlsx'

df1 = pd.read_csv(neo_file,index_col=False)
df2 = pd.read_excel(mapping,sheet_name='Mapping',index_col=False,engine='openpyxl')
df2 = df2[['Hotelcode','Chain Name','Activation Status']]
df3 = pd.merge(df1,df2,left_on='hotelcode',right_on='Hotelcode',how='inner')