# FUNCTION, BUTTON, TITLE, LABEL, ENTRY BOX, HEADER, COMBO BOX, CHECK BUTTON
# FRAME, MESSAGE BOX, LIST BOX

import calendar
from ntpath import join
import tkinter as tk
from tkinter import ANCHOR, BOTTOM, END, LEFT, Checkbutton, Listbox, StringVar, ttk, messagebox

from pandas import wide_to_long
from setuptools import Command

win = tk.Tk()

# FRAME # NOT COMPLETE # NOT CLEAR
frm_left = ttk.Frame(win,width=200,height=100)
frm_left.pack(side=BOTTOM)

fm1 = tk.Frame(win)
fm1.pack(fill=tk.BOTH, expand=1)

fm2 = tk.Frame(win)
fm2.pack(fill=tk.BOTH, expand=1)

# WINDOW SIZE
win.maxsize(width= 800,height = 600)
win.minsize(width=800,height=400)

# CHECK BUTTON
chkbtn1 = tk.IntVar()
chkbtn2 = tk.IntVar()
select = ttk.Checkbutton(win,text="Male",variable=chkbtn1,onvalue=1,offvalue=0)
select.place(x=150,y=110)
select = ttk.Checkbutton(win,text="Female",variable=chkbtn2,onvalue=1,offvalue=0)
select.place(x=210,y=110)

# COMBO BOX
v1 = StringVar()
cbox1 = ttk.Combobox(win,width=27,textvariable=v1)
cbox1['state'] = 'readonly'     # it's lock typing text in combo box
month_list = []
for i in range(1, 13): month_list.append(calendar.month_abbr[i])

cbox1['value'] = month_list
cbox1.current(0)    # set combo box 0 index value
cbox1.place(x=150,y=80)

# LABEL
lbl1 = tk.Label(fm1, text="SMPLE USER FORM" ,font=40)    # TITLE 
lbl1.place(x=250,y=10)
lbl2 = tk.Label(fm1, text="User Name", bg="black", fg="white",font=6)
lbl2.place(x=30,y=40)
lbl4 = tk.Label(fm1, text="Combo Box",bg="black", fg="white",font=6)
lbl4.place(x=30,y=80)
lbl3 = tk.Label(fm1,text="List Box", bg="yellow", fg="black")
lbl3.place(x=580,y=40,width=100)
lbl5 = tk.Label(win,text="Check Box",bg="red", fg="white").place(x=30,y=110)

# MESSAGE BOX  #  WITH FUNCTION
def func2():
    if ebox1_txt.get()  == "":
        messagebox.showwarning("WARING","PLEASE FILL ENTRY BOX")
    else:
        # messagebox.showinfo("Info Title", ebox1_txt.get())
        messagebox.askyesno("WANT TO EXIT","EXIT FOR YES ELSE NO")
        win.destroy()
def fun3():                         # FOR DELETE IN LIST
    lst1.delete(ANCHOR)             # FOR DELETE SELECTED VALUES IN LIST
def fun4():                         # show selected value in list
    show.config(text=lst1.get(ANCHOR))


lst = ['Sunday','Monday','Tuesday','WEDNESDAY','THUSDAY','FRIDAY','SATURDAY']
# LIST BOX 
lst1 = Listbox(win,width=30)
for r,i in enumerate(lst): lst1.insert(END,(f'{r+1} - {i}'))      # LAMBDA FOR LOOP FUNCTION
lst1.place(x=580,y=70, width=100)




# ENTRY BOX
ebox1_txt = tk.StringVar()
ebox1 = tk.Entry(win, text="Enter Your Txt Here", bg="white", width=30,textvariable=ebox1_txt )
ebox1.place(x=150,y=40, height=25)

# BUTTON
btn1 = tk.Button(win, text="SUBMIT", bg="red")
btn1.place(x=150,y=220,height=25,width=110)
# btn_var = tk.StringVar()
btn2 = tk.Button(win,text="CLICK ME"  ,bg="red", command=func2)
btn2.place(x=300,y=220,width=110)
btn3 = tk.Button(win,text="DELETE", command=fun3,bg="YELLOW")
btn3.place(x=580,y=250)

win.mainloop()









