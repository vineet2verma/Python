from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import os
import pandas as pd
import win32com.client as wc

root = Tk()
root.geometry("700x500+600+60")
root.resizable(0,0)
root.title("")
h1 = [('Arial',16,'bold'),('Arial',14,'bold'),('Arial',12,'bold'),('Arial',10,'bold'),('Arial',8,'bold'),('Arial',6,'bold')]
bg1 = "#222222"
sh_list,col_list = [],[]
filepath,filename,T_record = StringVar(),StringVar(),StringVar() #Entry Box
com1_var,com2_var = StringVar(),StringVar() # Combo Box
radio_var = StringVar() # Radio Box
xl_u_val = []
f2 = Frame(bg=bg1)
def home():
    f1 = Frame(bg=bg1)
    f1.place(x=0,y=0,height=500,width=700)
    l1 = Label(f1,text="WELCOME TO CLOVE DENTAL",font=h1[0])
    l1.pack(pady=20)
    btn1 = Button(f1,font=h1[2],text="CLICK ME",command=None)
    btn1.pack(pady=20)
def exit():
    xlapp.Quit()
    root.destroy()
def reset():
    print('reset run')
    if filepath !="":
        filename.set("")
        filepath.set("")
        T_record.set("")
        com1_var.set("")
        com2_var.set("")
        radio_var.set("")
def click_btn2():
    fname = filedialog.askopenfilename()
    filename.set(os.path.basename(fname))
    filepath.set(fname)
    sheet_name(fname)
def file_selection():
    f2.place(x=0,y=0,height=500,width=700)
    btn2 = Button(f2,font=h1[3],text="Select a File to be Destribution",command=click_btn2)
    btn2.place(x=10,y=10)
def entry_box():
    l2 = Label(f2,text="Total Record In The Below File  :",bg=bg1,fg='white',font=h1[3])
    l2.place(x=390,y=10,height=28)
    ent1 = Entry(f2,font=h1[4],text = T_record)
    ent1.place(x=618,y=10,height=28,width=60)
    l3 = Label(f2,text="File Path",font=h1[3],bg=bg1,fg='white')
    l3.place(x=10,y=50)
    ent2 = Entry(f2,font=h1[3],fg="black",textvariable=filepath)
    ent2.place(x=10,y=75,width=670)
    l4 = Label(f2,text="File Name",font=h1[3],bg=bg1,fg='white')
    l4.place(x=10,y=110)
    ent3 = Entry(f2,font=h1[3],fg="black",textvariable=filename)
    ent3.place(x=10,y=135,width=670)

l4 = Label(f2,text="Select A Sheets From the Above Workbook",font=h1[3],bg=bg1,fg='white')
l4.place(x=10,y=175)
com1 = ttk.Combobox(f2,font=h1[3],textvariable=com1_var)
com1.place(x=516,y=175)
l5 = Label(f2,text="Select Cateria Field From the Above Selected Worksheet",font=h1[3],bg=bg1,fg='white')
l5.place(x=10,y=215)
com2 = ttk.Combobox(f2,font=h1[3],textvariable=com2_var)
com2.place(x=516,y=215)

def combo_1():
    com1.config(values=sh_list)
def combo_2():
    com2.config(values=col_list)
def radio():
    l6 = Label(f2,text="Do You Want A Seperate File Or Sheets For Data Select Options As Req.",font=h1[3],bg=bg1,fg='white')
    l6.place(x=10,y=260)
    r1 = ttk.Radiobutton(f2,text="Workbook",value="Wb",variable=radio_var)
    r1.place(x=515,y=260)
    r2 = ttk.Radiobutton(f2,text="Worksheet",value="Ws",variable=radio_var)
    r2.place(x=598,y=260)
def btn():
    btn3 = Button(f2,text="HOME / RESET",font=h1[3],command=reset)
    btn3.place(x=10,y=400,width=150)
    btn4 = Button(f2,text="Distribute as File / Sheet",font=h1[3],command=destribute)
    btn4.place(x=250,y=400,width=200)
    btn5 = Button(f2,text="EXIT",font=h1[3],command=exit)
    btn5.place(x=525,y=400,width=150)
def c1_update(e):
    col_header()
    c1_val = e.widget.get()
    combo_2()
def sheet_name(filepath):
    allsheets = pd.ExcelFile(filepath).sheet_names
    for sh in allsheets: sh_list.append(sh)
    com1.config(values=sh_list)
com1.bind("<<ComboboxSelected>>",c1_update)
def col_header():
    # sh_sel = com1_var.get()
    df1 = pd.read_excel(filepath.get(),sheet_name=com1_var.get())
    print(len(df1))
    col_list.clear()
    for i in df1.columns: col_list.append(i)
    rows = len(df1)
    T_record.set(rows)
    com2_var.set("")

xlapp = wc.Dispatch("Excel.Application")
def destribute():
    print("Distribution Run.")
    os.chdir(os.path.dirname(filepath.get()))
    print(os.getcwd())
    if radio_var.get() == "Wb": workbook()
    elif radio_var.get() == "Ws": worksheet()

    wb = xlapp.Workbooks.Open(filepath.get())
    xlapp.Visible = True

def workbook():
    print("Workbook func")
    os.chdir(os.path.dirname(filepath.get()))
    wb_path = os.path.join(os.getcwd(),"Work Book")
    isExist = os.path.exists(wb_path)
    if not isExist: os.mkdir(wb_path)
    wb = xlapp.Workbooks.Open(filepath.get())
    xlapp.Visible = True
    col_index = col_list.index(com2_var.get())+1
    ws = wb.Worksheets(com1_var.get())
    # lst_row = ws.Cells(ws.Rows.Count, 1).End(-4162).Row  # lrow already in Trow
    # ws.Cells(1,col_index)

    for l1_val in xl_u_val:
        ws.Range("A:AP").AutoFilter(Field=col_index,Criteria1=l1_val)
        wb2 = xlapp.Workbooks.Add()
        ws2 = wb2.Worksheets(1)
        ws.Cells(1,1).CurrentRegion.Copy(ws2.Range('A1'))
        new_wb_path = os.path.join(os.getcwd(),"Work Book",l1_val+".xlsx")
        wb2.SaveAs(new_wb_path)
        wb2.Close()
    wb.Close(SaveChanges=False)

def worksheet():
    print("Worksheet func")
    os.chdir(os.path.dirname(filepath.get()))
    ws_path = os.path.join(os.path.dirname(filepath.get()),"Work Sheet")
    isExits = os.path.exists(ws_path)
    if not isExits: os.mkdir(ws_path)
    wb = xlapp.Workbooks.Open(filepath.get())
    xlapp.Visible = True
    col_index = col_list.index(com2_var.get()) + 1
    ws = wb.Worksheets(com1_var.get())

    for l1_val in xl_u_val:
        ws.Range("A:AP").AutoFilter(Field=col_index,Criteria1=l1_val)
        wb2 = xlapp.Workbooks.Add()
        ws2 = wb2.Worksheets.Add()
        ws2.Name = l1_val
        ws.Cells(1,1).CurrentRegion.Copy(ws2.Range('A1'))
        new_wb_path = os.path.join(os.getcwd(),"Work Sheet",l1_val+".xlsx")
        wb2.Worksheets("Sheet1").Delete()
        wb2.SaveAs(new_wb_path)
        wb2.Close()
    wb.Close(SaveChanges = False)

def c2_update(e):
    print(e.widget.get())
    df2 = pd.read_excel(filepath.get(),sheet_name=com1_var.get())
    xl_u_val.clear()
    for x in df2[com2_var.get()].unique(): xl_u_val.append(x)
com2.bind("<<ComboboxSelected>>",c2_update)

def text_box():
    txtinfo = """
    This is a text info
    """
    
    print("text_box")
    # tbox1 = Label(f2,text="This is Text Box Info")
    # tbox1.place(x=10,y=300)
    tbox2 = Text(f2,height=4,width=83)
    tbox2.place(x=10,y=300)
    tbox2.insert(END,txtinfo)

def main_running():
    file_selection()
    entry_box()
    combo_2()
    radio()
    btn()
    com1.bind("<<ComboboxSelected>>",c1_update)
    combo_1()
    text_box()

main_running()

root.mainloop()


