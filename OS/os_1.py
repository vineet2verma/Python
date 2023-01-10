# last modify file name & time

import glob
import os.path
import time

folder_path = r'd:\\RAW_DATA'
file_type = r'\*csv'
files = glob.glob(folder_path + file_type)

max_file = max(files, key=os.path.getctime)
print("File Name :- {0}".format(max_file))
date = time.strftime("%d-%m-%Y", time.localtime(os.path.getmtime(max_file)) )
print("Date : {0}".format(date))

