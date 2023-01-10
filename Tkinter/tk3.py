# TKINTER : FUNCTION, BUTTON, TITLE, LABEL, ENTRY BOX, HEADER

import tkinter as tk

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
# LABEL
lbl1 = tk.Label(win, text="SAMPLE USER FORM" ,font=40)    # TITLE 
lbl1.place(x=250,y=10)
lbl2 = tk.Label(win, text="User Name", bg="black", fg="white",font=10)
lbl2.place(x=30,y=40)

lbl3 = tk.Label(win,text="text 1", bg="red", fg="white")
lbl3.place(x=30,y=100)

# ENTRY BOX
ebox1_txt = tk.StringVar()
ebox1 = tk.Entry(win, text="Enter Your Txt Here", bg="white", width=30,textvariable=ebox1_txt )
ebox1.place(x=150,y=40, height=25)

# BUTTON
btn1 = tk.Button(win, text="SUBMIT", bg="red", command=func1)
btn1.place(x=150,y=200,height=25,width=110)

win.mainloop()









