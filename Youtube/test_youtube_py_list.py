from itertools import count
from time import sleep
from pytube import YouTube
from colorama import init, Fore
from pytube import Playlist
import webbrowser as wb
 
myurl = 'https://www.youtube.com/watch?v=T10v0L_c8bU&list=PLnZQydCjRQJzVS27vVBGTbgbiFP_tyXaD&index=1'
 
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
       
txt_file = 'd:\\'+pl_list_title+".txt"
    
with open(txt_file,"a+") as file:
    for i,x in enumerate(link):
        print(f"{i+1} {YouTube(x).title}")
        file.write(f"{i+1}\t{YouTube(x).title} | {x}"+"\n")

wb.open(txt_file)