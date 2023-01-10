# OPEN EXCEL WORKBOOK # GET ALL SHEET NAME  

from sqlite3 import Row
import openpyxl
from openpyxl import Workbook
from openpyxl.utils import column_index_from_string
from pyparsing import col
from pytest import Item

file1 = "C:\CHKING\INDEX_MATCH\HOTEL_NAME.xlsx"
file2 = "C:\CHKING\INDEX_MATCH\MASTER.xlsx"
wb1 = openpyxl.load_workbook(file1)
wb2 = openpyxl.load_workbook(filename=file2)

#  GET ALL SHEETS NAME IN WORKBOOK
sheets1 = wb1.sheetnames
#  CALL SHEET BY NAME
sh1_1 = wb1["SHEET_2"]
# GET SHEET CELL VALUE
# val = sh1_1["A2"].value     # val = sh2.cell(row=2,column=1).value

maxrow =  sh1_1.max_row    # MAX ROW
maxcol = sh1_1.max_column  # MAX COL

# CREATE SHEET
# wb2.create_sheet("testing")
n= 0
# FOR DATA PASTING SHEET CALL BY NAME
sh2_1 = wb2["testing"]
    
li = ['delhi','mumbai']

for row in sh1_1.iter_rows():
    if row[2].value in li :     # FILTER OR CONDITIONAL DATA PICKING
        # sh2_1.append([ row[0].value,row[2].value ])   # ALSO WORKING FOR DATA PASTE PERTICULAR CELL OR ROW
        sh2_1.append((cell.value for cell in row)) # PASTE ALL VALUES ( MULTIPLE ROW & MULTIPLE COL) 

Workbook.save(wb1,file1) 
Workbook.save(wb2,file2)    
