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
wb2 = openpyxl.load_workbook(file2)

#  CALL SHEET BY NAME
sh1_1 = wb1["SHEET_2"]
sh2_2 = wb2["testing"]
sh2_1 = wb2["ID"]

maxrow  = sh1_1.max_row     # MAX ROW
maxcol  = sh1_1.max_column  # MAX COL

# CREATE SHEET
# wb2.create_sheet("testing")
    
li = ['delhi','mumbai']     # USER FOR FILTER BASE CONDITION

# for row in sh1_1.iter_rows():
#     if row[2].value in li :     # FILTER OR CONDITIONAL DATA PICKING
#         # sh2_2.append([ row[0].value,row[2].value ])   # ALSO WORKING FOR DATA PASTE PERTICULAR CELL OR ROW
#         sh2_2.append((cell.value for cell in row)) # PASTE ALL VALUES ( MULTIPLE ROW & MULTIPLE COL) 



#  FOR INSERT COLUMN
# sh2_1.insert_cols(3,2)

# FOR DELETE COLUMN
# sh2_1.delete_cols(3,1)

# FOR INSERT ROW 
# sh2_1.insert_rows(3, 2)

# FOR DELETE ROW
# sh2_1.delete_rows(3,2)





Workbook.save(wb1,file1) 
Workbook.save(wb2,file2)    
