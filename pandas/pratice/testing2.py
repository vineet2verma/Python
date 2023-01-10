import pandas as pd
import openpyxl 
import numpy as np
import xlsxwriter

max = "C:\CHKING\Pratice_folder\max score.csv"
stu = "C:\CHKING\Pratice_folder\student.csv"
new_file = "C:\CHKING\Pratice_folder\student1.xlsx"

    # DATA FRAME
df_max = pd.read_csv(max)
df_stu = pd.read_csv(stu)
    # DATA FRAME = VLOOKUP 
df_ = df_stu.merge(df_max,how="inner", on="First Name")
# print(df_)
    # for create new workbook
# df_.to_excel(new_file,sheet_name="stu3",index=False)

    # for create new sheet in existing wb
# writer = pd.ExcelWriter(new_file,engine='xlsxwriter')
# df_.to_excel(writer,sheet_name="Sht1234")
# writer.save()

# append exist excel sheet
# with pd.ExcelWriter(new_file,engine='openpyxl', mode='a') as writer:
#     df_.to_excel(writer,sheet_name="xxx2",index=False)

# withpd.ExcelWriter('sample.xlsx', engine='openpyxl', mode='a') aswriter:  
#     df2.to_excel(writer, sheet_name='x2')

# working
# read all existing sheets and write them back
writer = pd.ExcelWriter(new_file, engine='xlsxwriter')
xlsx = pd.ExcelFile(new_file)
for sheet in xlsx.sheet_names:
    df = xlsx.parse(sheet_name=sheet, index_col=0)
    print(df)
    # df.to_excel(writer, sheet_name=sheet)