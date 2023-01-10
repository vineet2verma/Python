
# BAL 
# TRYING SPECIFY MAIL AND SAVE ATTACHMENT IN A FOLDER
# DONE 
# EXTRACT ZIP FILE AND SAVE IT SPECIFY FOLDER          


from operator import index
from traceback import print_tb
from zipfile import ZipFile
import os
import datetime as dt

cdate = dt.datetime.today().strftime("%d_%m_%y")
folder_path = "C:\\Inventory__\\" + cdate 
if os.path.isdir(folder_path) is False:
    os.makedirs(folder_path)

# zip file list
file_name = ["C:\Inventory__\INV_Depth.zip","C:\Inventory__\INV_Spread.zip"]

for index,f_name in enumerate(file_name):
    zip_file = ZipFile(f_name,"r")
    zip_file.extractall(folder_path)
    print(f"{index+1} :-\t {f_name} ")
