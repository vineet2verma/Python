# Tkinter frame base window with folder selection GUI

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from turtle import bgcolor, width

from numpy import pad

root = Tk()
root.geometry("1280x900")           # screen size
root.config(bg="light gray")        # background colour
root.minsize(width=1200,height=900)
root.maxsize(width=1200,height=900)
root.title("Youtube")
# root.iconbitmap("C:\Python\icons\youtube.ico")


# FRAME LOGO
frm0 = tk.Frame(bd=5,bg="sky blue",relief="sunken")
frm0.pack()
# LABEL
lbl_heading = tk.Label(frm0,text="You",font=("Arial Bold",20),fg="black",bg="white")
lbl_heading.grid(row=0,column=0)

lbl_heading = tk.Label(frm0,text="Tube",font=("Bold",20),fg="white",bg="red")
lbl_heading.grid(row=0,column=1)

border = tk.Frame(root,bd=2,bg="sky blue",width=1200,height=900)
border.pack(pady=5)

# MAIN FRAME
mainframe = tk.Frame(border, bg="sky blue",width=1100,height=900)
mainframe.pack(padx=10,pady=10,fill=Y)

# LABEL
lbl_btn = tk.Label(mainframe,text="Select File Type : ",bg="sky blue",font=("Arail",10,"bold"))
lbl_btn.grid(row=1,column=1)
# BUTTON
btn1 = tk.Button(mainframe,text='Single',font=("Arial",10,"bold"),bg="dark cyan",width=15)
btn1.grid(row=1,column=2,sticky=W)
btn2 = tk.Button(mainframe,text='Playlist ',font=("Arial",10,"bold"),bg="dark cyan",width=15)
btn2.grid(row=1,column=3,sticky=E)

linkbox = StringVar()
lbl_link = tk.Label(mainframe,text="YouTube Link :    ", bg="sky blue",font=("Arail",10,"bold"))
lbl_link.grid(row=2,column=1,pady=10,sticky=W)
ent_link = tk.Entry(mainframe,textvariable=linkbox,width=80,bd=2,bg="yellow")
ent_link.grid(row=2,column=2,pady=10,columnspan=3,sticky=W)

def browse_fun():
        file = filedialog.askdirectory()
        if len(file)>0: destbox.set(file+"/")

destbox = StringVar()
lbl_dest = tk.Label(mainframe,text="Dest. Path : ",bg="sky blue",font=("Arail",10,"bold"))
lbl_dest.grid(row=3,column=1, sticky=W)
ent_dest = tk.Entry(mainframe,bg="yellow",textvariable=destbox,width=80)
ent_dest.grid(row=3,column=2,columnspan=2)
btn_browse = tk.Button(mainframe,text="Browse",bg="dark cyan",font=("Arail",10,"bold"),width=15,command=browse_fun)
btn_browse.grid(row=3,column=3,sticky=E)

# FUNCTION
def exit_fun(): root.destroy()

def reset_fun(): 
    if destbox.get() !="":
        destbox.set("")
        linkbox.set("")

# RUN FRAME
submitframe = tk.Frame(border,bd=5,bg="sky blue",width=1200,height=800)
# submitframe.place(x=10,y=120)
submitframe.pack()

# SUBMIT BUTTON

submit_btn = tk.Button(submitframe,text="Submit",bg="green",width=15, font=("Arail",10,"bold"))
submit_btn.grid(row=1,column=1)

reset_btn = tk.Button(submitframe,text="Reset",bg="yellow",width=15,font=("Arail",10,"bold"),command=reset_fun)
reset_btn.grid(row=1,column=2,padx=107)

exit_btn = tk.Button(submitframe,text="Exit",bg="red",width=15,font=("Arail",10,"bold"),command=exit_fun)
exit_btn.grid(row=1,column=3)

# LIST/TREE FRAME
tree_frame = tk.Frame(root,bg="lightblue")
tree_frame.pack(pady=10)

tree_lbl = tk.Label(tree_frame,text="INFO GIVEN BELOW",bg="red",fg="white",font=("Arail",15,"bold"))
tree_lbl.pack()

mycol = ["ID","INFO"]
tree_list = ttk.Treeview(tree_frame,columns=mycol,show="headings"   )

tree_list.heading('ID',text='ID')
tree_list.heading('INFO',text='INFO')
tree_list.column('ID',width=50,anchor=W)
tree_list.column('INFO',width=100,anchor=CENTER)

tree_list.pack(pady=5)

# Msg Windows





root.mainloop()