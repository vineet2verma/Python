import os 
import webbrowser as wb

print("run")
file = "d:\\notepad.txt"

# For Writing In Notepad
with open(file,'a') as f:
    f.write(f"\n1")

wb.open(file)




