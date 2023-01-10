import time
import datetime
import schedule

ctime = datetime.datetime.now().strftime("%y/%m/%d - %I:%M:%S:%p") 

def show_me():
    print(f"show_me  ....  {datetime.datetime.now().strftime('%y/%m/%d - %I:%M:%S:%p')}") 
schedule.every(4).seconds.do(show_me)   

while 1:
    schedule.run_pending()