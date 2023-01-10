import os 
import webbrowser as wb
import time

print("run")
file = "d:\\notepad.txt"

search_text = "vineet"

# Reading Line by Line
# with open(file) as f:
#     for line_no, line in enumerate(f):
#         if search_text in line:
#             # print(line)
#             data = line.replace("vineet","vineet verma")
#             break

# replace data in an object
with open(file, "r") as f:
    data = f.read()
    data = data.replace(search_text,"vineet verma")

# overwrite data in same file
with open(file, "w") as f:
    f.write(data)
            
wb.open(file)






