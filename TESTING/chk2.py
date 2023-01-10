from itertools import count
from time import sleep
from pytube import YouTube
from colorama import init, Fore
from pytube import Playlist
 
choose1 = int(input("Press 1 :- Single File\nPress 2 :- Playlist\n\t"))

if choose1 == 1:
    print("Selection 1: Single File")
    link = input("Enter Url Link:-\n")
    print(type([link]))
    print(len(link))
    print(link.count(","))
elif  choose1 == 2:
    print("Selection 2: Playlist")
    link = input("Enter Url Link:-\n")
    print(type([link]))
    print(len(link))
    print(link.count(","))
else:
    print("Wrong Input")
    sleep(2)
    exit()

count = link.count(",")

