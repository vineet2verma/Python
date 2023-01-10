from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime as dt
import time

root = Tk()
root.geometry("600x600+550+60")
root.resizable(0,0)
root.title("")
font1 = ('Arial',12,'bold') 
sign_u_entry = StringVar()
sign_pswd = StringVar()
submit_entry = StringVar()

def btn_Hover(button, on_enter,on_leave):    
    button.bind("<Enter>", func=lambda e: button.config(bg=on_enter))
    button.bind("<Leave>", func=lambda e: button.config(bg=on_leave))
def exit():
    root.destroy()
    

def main():
    
    def time():
        my_time = dt.now().strftime("%H:%M:%S %p")
        lbl_time.config(text=my_time,fg="white")
        lbl_time.after(1000,time)
    
    frame1 = Frame(bg="#333333")
    frame1.place(x=0,y=0,width=600,height=600)
    lbl_time = Label(frame1,bg="#333333",font=('Arial',10,'bold'))
    lbl_time.place(relx=0.85)
    time()
    lbl_home = Label(frame1,text="PROJECT TABLE",font=('Arial',16,'bold'),bg='#333333',fg="red")
    lbl_home.place()
    btn_signup = Button(frame1, text="SIGN IN",width=15,padx=50,font=font1,command=cb2)
    btn_signup.pack(pady=10)
    btn_Hover(btn_signup,"green","white")
    table_sel()
    listbox()

l1 = []
for x in range(0,11): l1.append(x+1)

def cb2():
    aa = cbval.get()
    return aa
    
cbval = IntVar()
def table_sel():    
    f2 = Frame(bg="lightgrey")
    f2.place(x=0,y=100,width=600,height=600)
    cb1 = ttk.Combobox(f2,values=l1,textvariable=cbval)
    cb1.place(x=10,y=20)

def listbox():
    f3 = Frame(bg="lightblue")
    f3.place(x=200,y=100,height=600,width=400)
    lbl1 = Label(f3,text="Hello",font=font1)
    lbl1.pack()
    list1 = Listbox(f3)
    a = cb2()
    for x in range(10,0,-1):
        list1.insert(0,f"{a} * {x} = {a*x}")
    list1.place(x=20,y=20,height=200)

    list1.after(1000,listbox)


    


# tree_()
# print("hello  ",combo_var)
# def tree_():
#     f3 = Frame(bg="lightblue")
#     col = (1,2,3)
#     f3.place(x=180,y=100,width=450,height=600)
#     t1 = ttk.Treeview(f3,columns=col,show="headings")
#     for i in range(len(col)):
#         t1.column(col[i],width=50,anchor=CENTER)
#         t1.heading(col[i],text=i+1)
#         a = combo_var
#     for x in range(0,11):
#         t1.insert('',tk.END,values=(f'{a}',f'{a}=',f'{a}'))
#     t1.place(x=50,y=20,width=300,height=300)
    



# def signin():
#     frame2 = Frame(bg="#333333")
#     frame2.place(x=0,y=0,width=500,height=600)
#     lbl_submit = Label(frame2,text="LOGIN DETAILS",bg='#333333',fg='white',font=font1)
#     lbl_submit.place(x=160,y=20)
#     lbl_uname = Label(frame2,text="User Name",fg='black',bg='#333333',font=font1)
#     lbl_uname.place(x=75,y=100)    
#     ent_uname = Entry(frame2,text=sign_u_entry,fg='black',width=35)
#     ent_uname.place(x=200,y=100)
#     ent_uname.insert(0," ")
#     lbl_pswd = Label(frame2,text="Password",fg='black',bg='#333333',font=font1)
#     lbl_pswd.place(x=75,y=130)
#     ent_pswd = Entry(frame2,text=sign_pswd,fg='black',width=35,show="*")
#     ent_pswd.place(x=200,y=130)
#     btn_sign = Button(frame2,width=15,text="EXIT",fg='black',command=exit)
#     btn_sign.place(x=250,y=180)
#     btn_Hover(btn_sign,"red","white")
#     btn_submit = Button(frame2,width=15,text="SUBMIT",fg='black',command=user_chk)
#     btn_submit.place(x=100,y=180)
#     btn_Hover(btn_submit,"green","white")
# def user_chk():
#     if sign_u_entry !="" and sign_pswd !="":
#         if str(sign_u_entry.get()).upper() in user_name_list and str(sign_pswd.get()) == password_list[0]:
#                 messagebox.showinfo("Login Success","You Have Successfully Login")
#                 submit_()
#         else: messagebox.showerror("Error","Invalid Login")

# def submit_():
#     frame3 = Frame(bg="#333333")
#     frame3.place(x=0,y=0,height=600,width=500)
#     lbl_submit = Label(frame3,text="EMPLOYEE DETAILS",bg='#333333',fg='white',font=font1)
#     lbl_submit.place(x=160,y=20)
#     entry_box = Entry(frame3,text=submit_entry,fg='blue',font=('Arial',10,'bold'),bg='white',width=39)
#     entry_box.place(x=110,y=75,height=30)
    
#     btn_exit = Button(frame3,width=15,text="EXIT",command=exit)
#     btn_exit.place(x=270,y=150)
#     btn_Hover(btn_exit,"red","white")
#     btn_submit = Button(frame3,width=15,text="SUBMIT",fg='black',command=data)
#     btn_submit.place(x=110,y=150)
#     btn_Hover(btn_submit,"green","white")


# def data():
#     if submit_entry.get() !='':
#         val = submit_entry.get()
#         submit_entry.set("")
#         print(val)
#         if messagebox.askquestion("OK Cancel",'Want to Exit ?') == 'yes': exit()
        

main()
root.mainloop()










