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
 
choose1 = int(input("Press 1 :- Single File\nPress 2 :- Playlist\t"))
if choose1 == 1:
    print("\nSelection 1: \t***\tSingle File\t***")
    link = [input("Enter Url Link:-\n")]
    
elif  choose1 == 2:
    print("\nSelection 2: \t***\tPlaylist\t***")
    link = input("Enter Url Link:-\t")
    py = Playlist(link)
    pl_list_title = py.title
    link = py.video_urls
else:
    print("Wrong Input")
    sleep(2)
    exit()

F_PATH = 'D://Python video//'

# This is Url Notepad Syntax.
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
    if choose1 == 1:    print(f'\n{index+1} Out of {len(link)} :- ')
    else:   print(f'\n{index+1} Out of {len(link)} :-  {py.title}')  
    
    def on_complete(stream, filepath):
        print('download complete')
        
    # Open Every Times When File Download
        # li1 = filepath.split("/")
        # li1.pop()
        # li2 = "/".join(li1)
        # wb.open(li2)
        
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
    print(Fore.RED + f'title:  \033[39m {video_object.title}')
    print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
    print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
    print(Fore.RED + f'author: \033[39m {video_object.author}')
    print('\n\t\t Downlaoding In Progress....\tPlease Wait\n')
    yt = YouTube(link_)
    print(yt.title)
    if len(link)>1: FILE_PATH = F_PATH + py.title +"//"
    else:
        FILE_PATH = F_PATH + "//"
     
    video_object.streams.get_highest_resolution().download(FILE_PATH)

    li1 = FILE_PATH.split("/")
    li1.pop()
    li2 = "/".join(li1)
    # Folder Open 
    wb.open(li2)

