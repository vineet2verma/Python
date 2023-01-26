import shutil
import os

dir1 = 'd:\\Python\\Video\\Python Tutorials\\'
os.chdir(os.path.dirname(dir1))
aa = os.getcwd()
print(aa)

for path,dir,files in os.walk(os.getcwd()):
    if path == aa:
        continue
    else:
        merge = os.path.join(path,files[0])
        print(merge)    # chking 
        shutil.move(merge,aa+"\\")    # for move
        # print(path)   # chhking
        # print(files)  # chhking
        
    
    







