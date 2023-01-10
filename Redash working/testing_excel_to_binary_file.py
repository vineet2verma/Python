import xlwings as xw
import os

file = 'C:\\CHKING\\2Neo_testing_.xlsm'
file2 = 'C:\CHKING'

def macro_run():
    wb = xw.Book(file)
    print("\n"+wb.name+"\n")
    wb.macro("Module1.Macro1").run()    # FOR RUN MACRO
    # wb.save()                         # SAVE WORKBOOK
    xw.apps.active.quit()               # CLOSE EXCEL
    # xl = xw.apps.active.quit()
    # xl.quit()
os.chdir(file2)
cwd = os.getcwd()
if not "hello.xlsb" in os.listdir(cwd): macro_run()