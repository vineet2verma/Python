import cv2, os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.geometry("650x250")           # screen size
root.config(bg="light blue")        # background colour
root.title("IMAGE RE-SIZE TOOL")
# icon_path = "C:\\Python\\icons\\images (1).ico"
# root.iconbitmap(icon_path)

# FRAME LOGO
frm0 = tk.Frame(bd=5,bg="sky blue",relief="sunken")
frm0.pack()
# LABEL 
lbl_heading = tk.Label(frm0,text=" IMAGE ",font=("Arial Bold",20),fg="white",bg="black")
lbl_heading.grid(row=0,column=0)
lbl_heading = tk.Label(frm0,text=" RE-SIZE ",font=("Arial Bold",20),fg="white",bg="red")
lbl_heading.grid(row=0,column=1)

border = tk.Frame(root,bd=2,bg="sky blue",width=1200,height=900)
border.pack(pady=15)

# MAIN FRAME
mainframe = tk.Frame(border, bg="sky blue",width=800,height=900)
mainframe.pack(padx=10,pady=10,fill=Y)

# LABEL
lbl_btn = tk.Label(mainframe,text="Select  : ",bg="sky blue",font=("Arail",10,"bold"))
lbl_btn.grid(row=1,column=1,sticky=W)

# TEXT BOX
txt1_lbl = tk.Label(mainframe,height=1,text="Height",bg='sky blue',font=("Arial",10,"bold"))
txt1_lbl.grid(row=1, column=2,sticky=W)

txt1 = tk.StringVar()
txt1.set(1500)
txt1 = tk.Entry(mainframe,textvariable=txt1, width=10,bg="yellow", justify=CENTER, font=("Arial",10,"bold"))
txt1.grid(row=1, column=2,sticky=N)
txt2 = tk.StringVar()
txt2.set(1500)
txt1_lb2 = tk.Label(mainframe,height=1,text="Width",bg='sky blue',font=("Arial",10,"bold"))
txt1_lb2.grid(row=1, column=3,sticky=W)
txt2 = tk.Entry(mainframe,textvariable=txt2,bg="yellow",width=10,justify=CENTER, font=("Arial",10,"bold"))
txt2.grid(row=1, column=3,sticky=N)

def browse_fun():
        file = filedialog.askdirectory()
        if len(file)>0: destbox.set(file+"/")

destbox = StringVar()
lbl_dest = tk.Label(mainframe,text="Select Image Folder : ",bg="sky blue",font=("Arail",10,"bold"))
lbl_dest.grid(row=3,column=1, sticky=W,pady=10)
ent_dest = tk.Entry(mainframe,bg="yellow",textvariable=destbox,width=75)
ent_dest.grid(row=3,column=2,columnspan=2)
btn_browse = tk.Button(mainframe,text="Select",bg="red",font=("Arail",7,"bold"),width=10,command=browse_fun)
btn_browse.grid(row=3,column=3,sticky=E)

# FUNCTION
def exit_fun(): root.destroy()
def reset_fun(): 
    if destbox.get() !="":
        destbox.set("")
        # linkbox.set("")

def chk_folder():
    if not os.path.isdir(destbox.get() + '/output'):    os.mkdir(destbox.get() + '/output')
    image_resize()

def image_resize():
    li1 = ['jpg','jpeg','bmp']
    input_folder = str(destbox.get())
    output_folder = str(input_folder) + '\\output\\'
    os.chdir(input_folder)
    for i in os.listdir(input_folder):
        if os.path.abspath(i).endswith(tuple(i for i in tuple(li1))):
            fi = os.path.abspath(i)
            img = cv2.imread(fi)
            width = int(txt2.get())
            height= int(txt1.get())
            dimension = (width,height)
            resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
            print(resized.shape)
            cv2.imwrite(output_folder + i,resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    reset_fun()

# RUN FRAME
submitframe = tk.Frame(border,bd=5,bg="sky blue",width=1200,height=400)
submitframe.place(x=10,y=120)
submitframe.pack()

# SUBMIT BUTTON
submit_btn = tk.Button(submitframe,text="Submit",bg="green",width=15, font=("Arail",10,"bold"),command=chk_folder)
submit_btn.grid(row=1,column=1)

reset_btn = tk.Button(submitframe,text="Reset",bg="yellow",width=15,font=("Arail",10,"bold"),command=reset_fun)
reset_btn.grid(row=1,column=2,padx=107)

exit_btn = tk.Button(submitframe,text="Exit",bg="red",width=15,font=("Arail",10,"bold"),command=exit_fun)
exit_btn.grid(row=1,column=3)

root.mainloop()