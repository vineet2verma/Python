# LABEL, COMBO BOX
# LIST BOX
# BUTTON, CHECK BOX
# 
# 


from time import sleep
import tkinter as tk
from tkinter import * 
from tkinter import ANCHOR, BOTTOM, END, LEFT, Checkbutton, Listbox, StringVar, ttk, messagebox
# from tkinter import filedialog
# from tkinter.filedialog import FileDialog
# from tkinter.tix import COLUMN, Tree
import datetime as dt
import calendar


c_time = dt.datetime.now().strftime("%H:%M:%S")
print(c_time)

weeks,months,day,year =[],[],[],[]
for i in range(1, 13): months.append(calendar.month_name[i])    # Months
for i in range(0,7): weeks.append(calendar.day_name[i])         # Weekdays
for i in range(1,32): day.append(i)

# Tkinter
win = tk.Tk()
win.minsize(width=800,height=600)

# Title
win.title("PROJ LABEL")
win.config(bg="lightblue")

# LABEL TEXT
lbl_top = Label(win,text="TKINTER HELP CODE'S",font=('Arial',12,'bold'),bg='grey',fg='yellow',height=1)
lbl_top.pack(fill='x')

# LABEL TIME
def time():
    c_time = dt.datetime.now().strftime("%H:%M:%S")
    lbl_time.config(text=c_time)
    lbl_time.after(1000,time)

lbl_time = Label(lbl_top,font=("Arial",12,'bold'),bg='grey',fg='black',height=1)
lbl_time.pack(anchor='ne')
time()

# LABEL TEXT WITH COMBO BOX (DROP DOWN)
lbl_month = Label(win,text="COMBO",font=('Arial',10,'bold'),bg='black',fg='Red',width=13)
lbl_month.place(x=10,y=30)
lbl_month_text = ttk.Combobox(win,values=months,width=19)
lbl_month_text.current(months.index(dt.datetime.today().strftime("%B")))    # defualt value selected by index
lbl_month_text.place(x=10,y=60)
lbl_weekday = Label(win,text="COMBO",font=('Arial',10,'bold'),bg='black',fg='Red',width=13)
lbl_weekday.place(x=10,y=90)
lbl_weekday_text = ttk.Combobox(win,values=weeks,width=19)
lbl_weekday_text.current(weeks.index(dt.datetime.today().strftime("%A")))   # defualt value selected by index
lbl_weekday_text.place(x=10,y=120)

# LISTBOX SINGLE SELECT
lbl_list_day = Label(win,text="LIST BOX",font=('Arial',12,'bold'),bg='black',fg='yellow')
lbl_list_day.place(x=10,y=150)
list_day = Listbox(win,selectmode=SINGLE,width=22)
for i in range(len(weeks)): list_day.insert(i,weeks[i])
list_day.place(x=10,y=180)
# LISTBOX MULTI SELECT # WORKING
# list_month = Listbox(win,selectmode=MULTIPLE,width=22)
# for i in range(len(months)): list_month.insert(i,months[i])
# list_month.place(x=160,y=180)

# BUTTON 
lbl_btn = Label(win,text="BOTTON",font=('Arial',12,'bold'),bg='black',fg='yellow')
lbl_btn.place(x=10,y=350)

btn_1 = tk.Button(win,text="Male",bg="yellow")
btn_1.place(x=10,y=380)
btn_2 = tk.Button(win,text="Exit",bg="Red")
btn_2.place(x=60,y=380)

# CHECK BUTTON
lbl_chkbtn = Label(win,text="CHK BTN",font=('Arial',12,'bold'),bg='black',fg='yellow')
lbl_chkbtn.place(x=10,y=420)

ch_btn1 = tk.Checkbutton(win,text="Yes",bg='green')
ch_btn1.place(x=10,y=450)
ch_btn2 = tk.Checkbutton(win,text="No",bg='red')
ch_btn2.place(x=60,y=450)

# RADIO BUTTON

# SCROLLING

# TREE
tree_lbl = Label(win,text="Tree List ",fg='Red',bg="black",font=('Arial',12,'bold'))
tree_lbl.place(x=170,y=40)
tree_list = ttk.Treeview(win,columns=('ID','NAME'),show='headings')
tree_list.column('ID',anchor=CENTER,width=20)
tree_list.heading('ID',text='ID')
tree_list.column('NAME',anchor=CENTER,width=70)
tree_list.heading('NAME',text='NAME')
for i in range(0,7): tree_list.insert("","end",text=i+1,values=(i,weeks[i]))
tree_list.place(x=170,y=70,width=250)


# ENTER BOX
lbl_entry = Label(win,text="Entry Txt",fg='Red',bg='yellow',font=('Arial',12,'bold'))
lbl_entry.place(x=170,y=300)
entry_box = tk.Entry(win,fg="blue")
entry_box.insert(0,"Type Your Text Here")
entry_box.place(x=170,y=330,height=30)

# 
lbl_tbl = Label(win,text="table",fg="blue",bg="black")
lbl_tbl.place(x=0,y=0,)



win.mainloop()
