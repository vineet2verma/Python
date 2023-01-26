# Tkinter frame base window with folder selection GUI

import string
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from turtle import width
from numpy import pad
from pip import main

from itertools import count
from time import sleep
from pytube import YouTube
from colorama import init, Fore
from pytube import Playlist
import webbrowser as wb

# FUNCTION
def single():
        myclick = "single"
        if destbox.get() == "":
                file = filedialog.askdirectory()
                destbox.set(file + "/")
        youtube(myclick)

def playlist():
        myclick = "playlist"
        if destbox.get() == "":
                file = filedialog.askdirectory()
                destbox.set(file + "/")
        youtube(myclick)

def browse_fun():
        file = filedialog.askdirectory()
        if len(file)>0: destbox.set(file+"/")

def reset_fun(): 
    if destbox.get() !="":
        destbox.set("")
        linkbox.set("")

root = Tk()
root.geometry("1280x900")           # screen size
root.config(bg="light gray")        # background colour
root.minsize(width=500,height=300)
root.title("Youtube")
# root.iconbitmap("C:\Python\icons\youtube.ico")

# FRAME LOGO
frm0 = tk.Frame(bd=5,bg="sky blue")
frm0.pack(pady=5)
# LABEL
lbl_heading = tk.Label(frm0,text="You",font=("Arial Bold",20),fg="black",bg="white")
lbl_heading.grid(row=0,column=0)
lbl_heading = tk.Label(frm0,text="Tube",font=("Bold",20),fg="white",bg="red")
lbl_heading.grid(row=0,column=1,sticky=W)

border = tk.Frame(root,bd=2,bg="sky blue",width=1200,height=800)
border.pack(pady=5)

# MAIN FRAME
mainframe = tk.Frame(border, bg="sky blue",width=1100,height=700)
mainframe.pack(padx=10,pady=10)

linkbox = StringVar()
lbl_link = tk.Label(mainframe,text="YouTube Link :    ", bg="sky blue",font=("Arail",10,"bold"))
lbl_link.grid(row=2,column=1,pady=10,sticky=W)
ent_link = tk.Entry(mainframe,textvariable=linkbox,width=80,bd=2,bg="yellow",font=("Arail",15))
ent_link.grid(row=2,column=2,pady=10,columnspan=3,sticky=W)

destbox = StringVar()

lbl_dest = tk.Label(mainframe,text="Dest. Path : ",bg="sky blue",font=("Arail",10,"bold"))
lbl_dest.grid(row=3,column=1, sticky=W)

ent_dest = tk.Entry(mainframe,bg="yellow",textvariable=destbox,width=80,font=("Arail",15)   )
ent_dest.grid(row=3,column=2,columnspan=2)
btn_browse = tk.Button(mainframe,text="Browse",bg="dark cyan",font=("Arail",10,"bold"),width=15,command=browse_fun)
btn_browse.grid(row=3,column=3,sticky=E)

# FUNCTION
def exit_fun(): root.destroy()

# LABEL
lbl_btn = tk.Label(mainframe,text="Select File Type : ",bg="sky blue",font=("Arail",10,"bold"))
lbl_btn.grid(row=4,column=1)

# BUTTON
btn1 = tk.Button(mainframe,text='Single',font=("Arial",10,"bold"),bg="dark cyan",width=15,command=single)
btn1.grid(row=4,column=2,sticky=W)
btn2 = tk.Button(mainframe,text='Playlist ',font=("Arial",10,"bold"),bg="dark cyan",width=15,command=playlist)
btn2.grid(row=4,column=2)

reset_btn = tk.Button(mainframe,text="Reset",bg="red",width=15,font=("Arail",10,"bold"),command=reset_fun)
reset_btn.grid(row=4,column=3)  
exit_btn = tk.Button(mainframe,text="Exit",bg="red",width=15,font=("Arail",10,"bold"),command=exit_fun)
exit_btn.grid(row=4,column=3,sticky=E)  

# TREE VIEW
mycolumn = ('TITLE', 'LENGTH','VIEW')
tree = ttk.Treeview(root,columns=mycolumn, show="headings")
# # ADDING COLUMN
tree.column('TITLE',width=100,anchor=CENTER)    # ANCHOR FOR TEXT ALIGMENT
tree.column('LENGTH',width=100,anchor=CENTER)    # ANCHOR FOR TEXT ALIGMENT
tree.column('VIEW',width=100,anchor=CENTER)    # ANCHOR FOR TEXT ALIGMENT

# # ADDING HEADING
tree.heading('TITLE',text='TITLE')       # HEADING COLUMN TEXT
tree.heading('LENGTH',text='LENGTH')       # HEADING COLUMN TEXT
tree.heading('VIEW',text='VIEW')       # HEADING COLUMN TEXT

# # PACKING
tree.pack(padx=500,pady=20)


def youtube(myclick):        
        if myclick == 'single':
                print("\nSelection 1: \t***\tSingle File\t***")
                link = [linkbox.get()]
        elif  myclick == 'playlist':
                print("\nSelection 2: \t***\tPlaylist\t***")
        link = linkbox.get()
        py = Playlist(link)
        pl_list_title = py.title
        link = py.video_urls
        info_dic={}
        
        # This is Url Notepad Syntax.
        F_PATH = destbox.get()

        if myclick == "single":
                choose1 = 1
        elif myclick = "playlist":
                choose1 = 2

        def fun_txt(link):
                if choose1 == 2:
                        txt_file = F_PATH+pl_list_title+".txt"
                # elif choose1 == 1:
                        # yt = YouTube(link)._title
                        # print(yt)
                        # txt_file = F_PATH + str(yt) +".txt"
                        with open(txt_file,"a+") as file:
                                for i,x in enumerate(link):
                                        print(f"{i+1} {YouTube(x).title}")
                                        file.write(f"{i+1}\t{YouTube(x).title} | {x}"+"\n")
                        wb.open(txt_file)
        fun_txt(link)
        
        
        
        for index,link2 in enumerate(link):
                if myclick == 'single':    print(f'\n{index+1} Out of {len(link)} :- ')
                else:   print(f'\n{index+1} Out of {len(link)} :-  {py.title}')  

                def on_complete(stream, filepath):
                        print('download complete')
                        li1 = filepath.split("/")   
                        li1.pop()
                        li2 = "/".join(li1) 
                        wb.open(li2)
                        
                def on_progress(stream, chunk, bytes_remaining):
                        progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
                        print(progress_string)
                init()
                print()
                link_ = link2
                print()
                video_object    = YouTube(link_, on_complete_callback = on_complete, on_progress_callback = on_progress)
                title = video_object.title
                # information
                info_dic['title']       =       str(video_object.title),
                info_dic['length']      =       str(round(video_object.length / 60,2)) + 'minutes',
                info_dic['views']       =       str(video_object.views / 1000000) + 'million'

                print(Fore.RED + f'title:  \033[39m {video_object.title}')
                print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
                print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
                print(Fore.RED + f'author: \033[39m {video_object.author}')
                print('\n\t\t Downlaoding In Progress....\tPlease Wait\n')
        
                download_choice = 'b'
                if len(link)>1: FILE_PATH = destbox.get() +"/" + py.title + "/"
                else:   FILE_PATH = destbox.get() + "/"
        
                match download_choice:
                        case 'b':       video_object.streams.get_highest_resolution().download(FILE_PATH)
                        case 'w':       video_object.streams.get_lowest_resolution().download(FILE_PATH)
                        case 'a':       video_object.streams.get_audio_only().download(FILE_PATH)

                # for key,value in info_dic:
                # tree.insert(root,END,values=( info_dic['TITLE'],info_dic['LENGTH'],info_dic['VIEW']      ) )        # ADDING VALUE IN TREE VIEW BY DICTIONARY


root.mainloop()