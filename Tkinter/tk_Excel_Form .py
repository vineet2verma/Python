from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import os
import pandas as pd
import win32com.client as wc

h1 = [('Arial',16,'bold'),('Arial',14,'bold'),('Arial',12,'bold'),('Arial',10,'bold')]
bg1 = "#333333"
style = ttk.Style()
style.configure('TRadiobutton',background=bg1,foreground="white",font=h1[3])
radio_var = StringVar()
com1_var = StringVar()
com2_var = StringVar()
t_record = StringVar()
f_path = StringVar()
f_name = StringVar()
f2 = Frame(bg=bg1)


file = r"C:\Users\Owner\Desktop\TEST\1 to 28 OCT.xls"
sh_list = []
col_list = ['col1','col2']

def col_names():
    if com1_var !="":
        col_list.append("1")

def xl_all_sh_Name():
    print("excel")
    xlapp = wc.Dispatch("Excel.Application")
    xlapp.Visible = True
    wb = xlapp.Workbooks.Open(file)
    for sh in wb.Sheets:
        sh_list.append(sh.Name)
    xlapp.Quit()
def xl_col_Name():
    pass
def xl_ws_dist():
    pass
def xl_wb_dist():
    pass

root = Tk()
root.geometry("700x500+600+60")
root.resizable(0,0)
root.title("")


def home():
    f1 = Frame(bg=bg1)
    f1.place(x=0,y=0,height=500,width=700)
    l1 = Label(f1,text="WELCOME TO CLOVE DENTAL",font=h1[0])
    l1.pack(pady=20)
    btn1 = Button(f1,font=h1[2],text="CLICK ME",command=None)
    btn1.pack(pady=20)
def exit():
    root.destroy()
def btn_file():
    print("File Press")
    file_info = filedialog.askopenfilename(title="Select A File")
    f_path.set(file_info)
    f_name.set(os.path.basename(file_info))
    
def btn_home():
    print("Home Press")
def btn_distribution():
    print("Distribution Press")
    print(radio_var.get())
    print(com1_var.get())
    print(com2_var.get())
    print(t_record.get())
    print(f_path.get())
    print(f_name.get())
def file_destribution():
    f2.place(x=0,y=0,height=500,width=700)
    btn2 = Button(f2,font=h1[3],text="Select a File to be Destribution",command=btn_file)
    btn2.place(x=10,y=10)
    l2 = Label(f2,text="Total Record in the Below File",bg=bg1,fg='white',font=h1[3])
    l2.place(x=360,y=10,height=28)
    ent1 = Entry(f2,font=h1[3],fg='black',text=t_record)
    ent1.place(x=600,y=10,height=28,width=80)
    l3 = Label(f2,text="File Path",font=h1[3],bg=bg1,fg='white')
    l3.place(x=10,y=50)
    ent2 = Entry(f2,font=h1[2],fg="black",text=f_path)
    ent2.place(x=10,y=75,width=670)
    l4 = Label(f2,text="File Name",font=h1[3],bg=bg1,fg='white')
    l4.place(x=10,y=110)
    ent3 = Entry(f2,font=h1[2],fg="black",text=f_name)
    ent3.place(x=10,y=135,width=670)
    l4 = Label(f2,text="Select A Sheets From the Above Workbook",font=h1[3],bg=bg1,fg='white')
    l4.place(x=10,y=175)
    com1 = ttk.Combobox(f2,font=h1[2],values=sh_list,textvariable=com1_var)
    com1.place(x=475,y=175)
    l5 = Label(f2,text="Select Cateria Field From the Above Selected Worksheet",font=h1[3],bg=bg1,fg='white')
    l5.place(x=10,y=215)
    com2 = ttk.Combobox(f2,font=h1[2],values=col_list,textvariable=com2_var)
    com2.place(x=475,y=215)
    l6 = Label(f2,text="Do you want a Seperate File or Sheets for data Select Options as Req.",font=h1[3],bg=bg1,fg='white')
    l6.place(x=10,y=260)
    
    r1 = ttk.Radiobutton(f2,text="Work Sheet",variable=radio_var,value="ws",style=('TRadiobutton'))
    r1.place(x=471,y=260)
    r2 = ttk.Radiobutton(f2,text="Work Book",variable=radio_var,value="wb",style=("TRadiobutton"))
    r2.place(x=585,y=260)
        
    btn3 = Button(f2,text="HOME",font=h1[3],command=btn_home)
    btn3.place(x=10,y=400,width=150)
    btn4 = Button(f2,text="Distribute as File / Sheet",font=h1[3],command=btn_distribution)
    btn4.place(x=250,y=400,width=200)
    btn5 = Button(f2,text="EXIT",font=h1[3],command=exit)
    btn5.place(x=525,y=400,width=150)

file_destribution()
root.mainloop()










