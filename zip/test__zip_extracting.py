# importing required modules
from zipfile import ZipFile
import os
import datetime as dt

cdate = dt.datetime.today().strftime("%d_%m_%y")
# specifying the zip file name
folder_path = "C:\\Inventory__\\" + cdate 

if os.path.isdir(folder_path) is False:
    os.makedirs(folder_path)

print(folder_path)
file_name = "C:\Inventory__\INV_Depth.zip"

# opening the zip file in READ mode
# with ZipFile(file_name, 'r') as zip:
# 	# printing all the contents of the zip file
# 	# zip.printdir()

# 	# extracting all the files
# 	print('Extracting all the files now...')
#     # zip.extractall()
# 	print('Done!')


zip_file = ZipFile(file_name,"r")
zip_file.extractall(folder_path)
print("Done")