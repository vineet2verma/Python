from statistics import mode
import openpyxl
from openpyxl import Workbook
import pandas as pd
from pyparsing import col
from pytest import skip

file1 = "C:/CHKING/INDEX_MATCH/MASTER.xlsx"
file2 = "C:/CHKING/INDEX_MATCH/HOTEL_NAME.xlsx"

wb1 = pd.read_excel(file1,sheet_name="SHEET123")    # master file
wb2 = pd.read_excel(file2,sheet_name="Sheet2")      # hotel name
list1 = []
# for know about col no.
for num,i1 in enumerate(wb1.columns):
    if i1 in wb2.columns:
        list1.append(num)


for i in list1:
    print(i)

# copy1 = wb1[list1].copy()
# print(copy1)
# paste data but remove old one
# copy1.to_excel(file2,sheet_name="Sheet2")

# it's create a new sheet and paste data
# with pd.ExcelWriter(file2,mode='a') as writer:
    # copy1.to_excel(writer,sheet_name="Sheet1")




