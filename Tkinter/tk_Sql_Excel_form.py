from tkinter import *
from tkinter import messagebox
import pyodbc as odbc
import pandas as pd
from datetime import datetime

date = datetime.today()
user_name_list = ['001','002','003','004',' ']
password_list = [" "]

root = Tk()
root.geometry("500x300+450+60")
root.resizable(0,0)
root.title("")
font1 = ('Arial',12,'bold') 
sign_u_entry = StringVar()
sign_pswd = StringVar()
submit_entry = StringVar()

def btn_Hover(button, on_enter,on_leave):    
    button.bind("<Enter>", func=lambda e: button.config(bg=on_enter))
    button.bind("<Leave>", func=lambda e: button.config(bg=on_leave))
def main():
    frame1 = Frame(bg="#333333")
    frame1.place(x=0,y=0,width=500,height=600)
    lbl_home = Label(frame1,text="WELCOME TO CLOVE DENTAL",font=('Arial',16,'bold'),bg='#333333',fg="red")
    lbl_home.place(x=85,y=20,width=310)
    btn_signup = Button(frame1, text="SIGN IN",width=15,padx=50,font=font1,command=signin)
    btn_signup.place(x=110,y=100)
    btn_Hover(btn_signup,"green","white") 
def exit():
    root.destroy()
def signin():
    frame2 = Frame(bg="#333333")
    frame2.place(x=0,y=0,width=500,height=600)
    lbl_submit = Label(frame2,text="LOGIN DETAILS",bg='#333333',fg='white',font=font1)
    lbl_submit.place(x=160,y=20)
    lbl_uname = Label(frame2,text="User Name",fg='black',bg='#333333',font=font1)
    lbl_uname.place(x=75,y=100)    
    ent_uname = Entry(frame2,text=sign_u_entry,fg='black',width=35)
    ent_uname.place(x=200,y=100)
    ent_uname.insert(0," ")
    lbl_pswd = Label(frame2,text="Password",fg='black',bg='#333333',font=font1)
    lbl_pswd.place(x=75,y=130)
    ent_pswd = Entry(frame2,text=sign_pswd,fg='black',width=35,show="*")
    ent_pswd.place(x=200,y=130)
    btn_sign = Button(frame2,width=15,text="EXIT",fg='black',command=exit)
    btn_sign.place(x=250,y=180)
    btn_Hover(btn_sign,"red","white")
    btn_submit = Button(frame2,width=15,text="SUBMIT",fg='black',command=user_chk)
    btn_submit.place(x=100,y=180)
    btn_Hover(btn_submit,"green","white")
def user_chk():
    if sign_u_entry !="" and sign_pswd !="":
        if str(sign_u_entry.get()).upper() in user_name_list and str(sign_pswd.get()) == password_list[0]:
                messagebox.showinfo("Login Success","You Have Successfully Login")
                submit_()
        else: messagebox.showerror("Error","Invalid Login")

def submit_():
    frame3 = Frame(bg="#333333")
    frame3.place(x=0,y=0,height=600,width=500)
    lbl_submit = Label(frame3,text="EMPLOYEE DETAILS",bg='#333333',fg='white',font=font1)
    lbl_submit.place(x=160,y=20)
    entry_box = Entry(frame3,text=submit_entry,fg='blue',font=('Arial',10,'bold'),bg='white',width=39)
    entry_box.place(x=110,y=75,height=30)
    
    btn_exit = Button(frame3,width=15,text="EXIT",command=exit)
    btn_exit.place(x=270,y=150)
    btn_Hover(btn_exit,"red","white")
    btn_submit = Button(frame3,width=15,text="SUBMIT",fg='black',command=data)
    btn_submit.place(x=110,y=150)
    btn_Hover(btn_submit,"green","white")


def data():
    print("data run")

    def sql(col_name,condition):
        conn = odbc.connect('Driver={SQL SERVER};' 'Server=VINEET-PC\SQLEXPRESS;' 'Database=hotel;' 'Trust_Connection=yes;')
        cursor = conn.cursor()
        
        cursor.execute(f"Select * from [hotel].[dbo].[Table_2] where {col_name} = '{condition}' ")
        for x in cursor:
            print(x)
        cursor.close()
    
    if submit_entry.get() !='':
        val = submit_entry.get()
        submit_entry.set("")
        # print(val)
        sql('hotelname',val)
        if messagebox.askquestion("OK Cancel",'Want to Exit ?') == 'yes': exit()

    

main()
root.mainloop()










