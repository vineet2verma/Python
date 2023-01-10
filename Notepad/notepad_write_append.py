import datetime as dt, time
from datetime import timedelta
import pandas as pd

start = dt.datetime.utcnow()
c_date = dt.datetime.now().strftime("%Y_%m_%d_%I_%M_%p")

comments = "this is line second"
text_list = [c_date,comments]

with open("c:\\Python\\code.txt","a+") as code_run:
    code_run.write("\n")
    for x in range(len(text_list)):
        code_run.write(text_list[x])
        code_run.write("\t")
        
print("today ",c_date)
