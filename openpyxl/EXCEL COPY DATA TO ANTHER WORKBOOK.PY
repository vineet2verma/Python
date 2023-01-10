# OPEN EXCEL WORKBOOK # GET ALL SHEET NAME  

from sqlite3 import Row
import openpyxl
from openpyxl import Workbook
from openpyxl.utils import column_index_from_string
from pyparsing import col
from pytest import Item

file1 = "C:\CHKING\INDEX_MATCH\HOTEL_NAME.xlsx"
file2 = "C:\CHKING\INDEX_MATCH\MASTER.xlsx"
file3 = "C:\CHKING\INDEX_MATCH\mapping_chk.xlsx"

wb1 = openpyxl.load_workbook(file1)
wb2 = openpyxl.load_workbook(filename=file2)
wb3 = openpyxl.load_workbook(file3)

# sh1 = wb1.get_sheet_by_name("Sheet2") # Sheet 2
sh2 = wb1['Sheet2']   #get_sheet_by_name("Sheet2") # hotel name
sh3 = wb3['Sheet1']  #.get_sheet_by_name("Sheet1")   # mapping sheet

list1 = []

for i in range(sh2.max_column):
    list1.append(sh2.cell(1,i+1).value)
print(list1)

for r in range(sh3.max_row):
    for i in range((sh2.max_column)):
        if sh3.cell(1,i+1).value in list1:
            coll = list1.index(sh3.cell(1,i+1).value)
            
            # print(sh3.cell(r+1,i+1).value)
            sh3.cell(r+1,coll+1).value = sh2.cell(1,i+1).value


# wb3.save(file3)

        

#  GET ALL SHEETS NAME IN WORKBOOK
# sheets1 = wb1.sheetnames

#  CALL SHEET BY NAME
# sh1_2 = wb1.get_sheet_by_name("Sheet")

# GET SHEET CELL VALUE
# val = sh1_2["A2"].value     # val = sh2.cell(row=2,column=1).value

# maxrow =  sh1_2.max_row    # MAX ROW
# maxcol = sh1_2.max_column  # MAX COL

# FOR PERTICULAR DATA CELLS
# for item in range(1,maxrow+1):
    # print(sh1_2.cell(row= item,column=1).value)

# FOR READING ALL CELLS DATA
# for ro in range (1,maxrow+1):
#     for co in range(1,maxcol+1):
#         print(sh1_2.cell(ro,co).value,end="") 
#     print()

# CREATE SHEET
# wb2.create_sheet("testing")
# n= 0

# FOR DATA PASTING SHEET CALL BY NAME
# sh3 = wb2.get_sheet_by_name("testing")

# DATA PASTE ONE SHEET TO ANOTHER WORKBOOK SHEET
# for ro in range (1,maxrow+1):
#     if sh1_2.cell(ro,3).value == "delhi":       # CONDITION BASE PASTEING
#         n = n+1     
#         for co in range(1,maxcol+1):
#             print(sh3.cell(n,co).coordinate) # Checking Cell Address
#             sh3.cell(n,co).value = sh1_2.cell(ro,co).value
    
# li = ['delhi','mumbai']
# # DATA APPEND OR PASTE AFTER LAST CELLS
# for ro in range (1,maxrow+1):    
#     if (sh1_2.cell(ro,3).value == "mumbai" or sh1_2.cell(ro,3).value == "delhi"):       # CONDITION BASE PASTEING
#         n = sh3.max_row + 1                     # 
#         for co in range(1,maxcol+1):
#             print(sh3.cell(n,co).coordinate) # Checking Cell Address
#             sh3.cell(n,co).value = sh1_2.cell(ro,co).value
            



# print(wb1.sheetnames)
# print(wb2.sheetnames)
# Workbook.save(wb1,file1) 
# Workbook.save(wb2,file2)    
