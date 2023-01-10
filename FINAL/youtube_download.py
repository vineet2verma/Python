from pytube import YouTube
import webbrowser as wb
from colorama import init, Fore
 
def on_complete(stream, filepath):
    print('download complete')
    print(filepath)
    li1 = filepath.split("/")
    li2 = li1.pop()
    li3 = "/".join(li1)
    wb.open(li3)
    print(li3)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
    print(progress_string)
 
init()
print()
link = input('Youtube link: \n')
print()
video_object    = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)


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
 
match download_choice:
    case 'b':
        video_object.streams.get_highest_resolution().download(r'C:/CHKING_2/python/')
    case 'w':
        video_object.streams.get_lowest_resolution().download(r'C:/CHKING_2/python/')
    case 'a':
        video_object.streams.get_audio_only().download(r'C:/CHKING_2/python/')
    
