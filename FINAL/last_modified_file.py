# OS MODULE -> CREATE FOLDER, CHKING FOLDER EXISTS, 
# ALL FOLDER & FILES, ALL FILES IN A FOLDER

import os
from time import ctime
import pandas as pd

Folder = 'C:\CHKING'

# FUNC. - FOR FOLDER CREATE
def create_folder(fol_name,file_name):
    folder = os.path.join(fol_name, file_name)
    os.mkdir(folder)

# FUNC = FOR CHECKING FOLDER EXISTS OR NOT
def chk_folder_exists(main_dir,fol_name):
    info =  os.listdir(main_dir)
    myans = 'No'
    for f in (info):
        if fol_name == f:   myans = 'Yes'            
    print(myans)

# FUNC = FOR ALL FOLDER & FILES IN FOLDER
def folder_all_files(Folder):
    fi = os.listdir(Folder)
    print(fi)

# FUCH = FOR ONLY FILES IN FOLDER
def folder_file_only(Folder):
    li = []
    for f in os.listdir(Folder):
        if f.__contains__("."): li.append(f)
    return li

def last_modified_file(Folder):
    folder_file_only(Folder)
    f1 = []
    f2 = []
    for f in folder_file_only(Folder):
        f_path = os.path.join(Folder, f)
        f1.append(ctime(os.path.getmtime(f_path)))
        # f2.append(f_path)
        print(f"{f} => {ctime(os.path.getmtime(f_path))}")
    # print(f1.index(max(f1)))
    # print()
    # print("\n" + f1)
    # print("\n"+f2)
    # print("\n"+f2[f1.index(max(f1))])


last_modified_file(Folder)



# ff1 = 'C:\\CHKING\\002.xlsx'
# print(
#     ctime(os.path.getctime(ff1))
# )
# print(
#     ctime(os.path.getmtime(ff1))
# )