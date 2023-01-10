# OPEN EXCEL WORKBOOK
# GET ALL SHEET NAME  
import openpyxl

file1 = "C:\CHKING\INDEX_MATCH\HOTEL_NAME.xlsx"
file2 = "C:\CHKING\INDEX_MATCH\MASTER.xlsx"

wb = openpyxl.load_workbook(file1)
#  GET ALL SHEETS NAME IN WORKBOOK
sheets = wb.get_sheet_names()
# sheets = wb.sheetnames   # BOTH ARE CORRECT
#  CALL SHEET BY NAME
sheet_by_name = wb.get_sheet_by_name("SHEET_2")

print( sheets )


