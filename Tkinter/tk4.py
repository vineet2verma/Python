# FUNCTION, BUTTON, TITLE, LABEL, ENTRY BOX, HEADER
# COMBO BOX

import tkinter as tk
from tkinter import StringVar, ttk
from matplotlib.pyplot import text

from matplotlib.widgets import Widget

win = tk.Tk()

# FUNCTION
def func1():
    x = ebox1_txt.get()     # GETTING VALUE FROM VARIABLE \
    print(x)
    lbl3.config(text =x)    

# TITLE
win.title("3")
# WINDOW SIZE
win.maxsize(width= 800,height = 600)
win.minsize(width=800,height=400)

# COMBO BOX
v1 = StringVar()
cbox1 = ttk.Combobox(win,width=27,textvariable=v1)
cbox1['state'] = 'readonly'     # it's lock typing text in combo box
cbox1['value'] = ['Jan','Feb','Mar']
cbox1.current(0)    # set combo box 0 index value
cbox1.place(x=150,y=80)

# LABEL
lbl1 = tk.Label(win, text="SAMPLE USER FORM" ,font=40)    # TITLE 
lbl1.place(x=250,y=10)
lbl2 = tk.Label(win, text="User Name", bg="black", fg="white",font=6)
lbl2.place(x=30,y=40)
lbl4 = tk.Label(win, text="Combo Box",bg="black", fg="white",font=6)
lbl4.place(x=30,y=80)
lbl3 = tk.Label(win,text="text 1", bg="red", fg="white")
lbl3.place(x=30,y=150,width=100)

# ENTRY BOX
ebox1_txt = tk.StringVar()
ebox1 = tk.Entry(win, text="Enter Your Txt Here", bg="white", width=30,textvariable=ebox1_txt )
ebox1.place(x=150,y=40, height=25)

# BUTTON
btn1 = tk.Button(win, text="SUBMIT", bg="red", command=func1)
btn1.place(x=150,y=200,height=25,width=110)

win.mainloop()









