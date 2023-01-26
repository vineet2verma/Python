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
for index,link2 in enumerate(link):
    if choose1 == 1:    print(f'\n{index+1} Out of {len(link)} :- ')
    else:   print(f'\n{index+1} Out of {len(link)} :-  {py.title}')  
    
    def on_complete(stream, filepath):
        print('download complete')
        print("filepath is :- ",filepath)
        
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
    print(Fore.RED + f'title:  \033[39m {video_object.title}')
    print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
    print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
    print(Fore.RED + f'author: \033[39m {video_object.author}')
    print('\n\t\t Downlaoding In Progress....\tPlease Wait\n')
    
    # download
    # print(
    #     Fore.RED + 'download:' + 
    #     Fore.GREEN + '(b)est \033[39m|' + 
    #     Fore.YELLOW + '(w)orst \033[39m|' + 
    #     Fore.BLUE + '(a)udio \033[39m| (e)xit')
    # download_choice = input('choice: ')
    download_choice = 'b'
    a = "/"+str(index+1)
    if len(link)>1: FILE_PATH = "D:/python/Video/" + py.title +a # "/"
    else:   FILE_PATH = "D:/python/Video/"
     
    match download_choice:
        case 'b':
            video_object.streams.get_highest_resolution().download(FILE_PATH)
            








# # from posixpath import split
# from pytube import YouTube
# from colorama import init, Fore
# import datetime,webbrowser
 

# def on_complete(stream, filepath):
#     print('download complete')
#     print(filepath)
#     li1 = filepath.split("/")
#     li2 = li1.pop()
#     li3 = "/".join(li1)
#     webbrowser.open(li3)
    
# def on_progress(stream, chunk, bytes_remaining):
#     progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
#     print(progress_string)
 
# init()
# link = input('\n\tYoutube link:\t\t ')
# video_object    = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# # information
# print(f'Title:  \033[39m {video_object.title}')
# print(f'Length: \033[39m {round(video_object.length / 60,2)} Minutes')
# print('\n\t\t Downlaoding In Progress....\tPlease Wait\n')
 
# # download_choice = 'b'
# video_object.streams.get_highest_resolution().download(r'C:/CHKING_2/python/')
