import os

cwd_path = os.getcwd()
print("old  " + cwd_path)
os.chdir("C:\Python")
changed = os.getcwd()
print("new  "+changed)

