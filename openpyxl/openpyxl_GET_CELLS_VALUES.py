# OPEN EXCEL WORKBOOK # GET ALL SHEET NAME  
# READ DATA AS PER CELLS VALUES
# DATA PASTE FROM ONE SHEET TO ANOTHER SHEET WITH CONDITION BASIC.


from sqlite3 import Row
import openpyxl
from openpyxl import Workbook
from openpyxl.utils import column_index_from_string
from pyparsing import col
from pytest import Item

file1 = "C:\CHKING\INDEX_MATCH\HOTEL_NAME.xlsx"
wb = openpyxl.load_workbook(file1)

#  GET ALL SHEETS NAME IN WORKBOOK
sheets = wb.sheetnames

#  CALL SHEET BY NAME
sh2 = wb.get_sheet_by_name("SHEET_2")

# GET SHEET CELL VALUE
val = sh2["A2"].value
# val = sh2.cell(row=2,column=1).value

maxrow =  sh2.max_row    # MAX ROW
maxcol = sh2.max_column  # MAX COL

# FOR PERTICULAR DATA CELLS
# for item in range(1,maxrow+1):
    # print(sh2.cell(row= item,column=1).value)

# FOR READING ALL CELLS DATA
for ro in range (1,maxrow+1):
    for co in range(1,maxcol+1):
        print(sh2.cell(ro,co).value,end="") 
    print()

# CREATE SHEET
# wb.create_sheet("testing")

sh3 = wb.get_sheet_by_name("testing")
n= 0
# DATA PASTE ONE SHEET TO ANOTHER SHEET
# for ro in range (1,maxrow+1):
#     if sh2.cell(ro,3).value == "delhi":       # CONDITION BASE PASTEING
#         n = n+1        for co in range(1,maxcol+1):
#             print(sh3.cell(n,co).coordinate) # Checking Cell Address
#             sh3.cell(n,co).value = sh2.cell(ro,co).value

print(wb.sheetnames)
Workbook.save(wb,file1) 
