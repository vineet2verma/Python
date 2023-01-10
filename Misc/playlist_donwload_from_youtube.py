from pytube import YouTube
from colorama import init, Fore
 
def on_complete(stream, filepath):
    print('download complete')
    print(filepath)
 
def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
    print(progress_string)
 
init()
print()
link = input('Youtube link: ')
print()
# video_object    = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)
playlist_object = Playlist(link,on_complete_callback= on_complete, on_progress_callback = on_progress)

# information
print(Fore.RED + f'title:  \033[39m {playlist_object.title}')
print(Fore.RED + f'length: \033[39m {round(playlist_object.length / 60,2)} minutes')
print(Fore.RED + f'views:  \033[39m {playlist_object.views / 1000000} million')
print(Fore.RED + f'author: \033[39m {playlist_object.author}')
 
# download
print(
    Fore.RED + 'download:' + 
    Fore.GREEN + '(b)est \033[39m|' + 
    Fore.YELLOW + '(w)orst \033[39m|' + 
    Fore.BLUE + '(a)udio \033[39m| (e)xit')
download_choice = input('choice: ')
 
match download_choice:
    case 'b':
        playlist_object.streams.get_highest_resolution().download(r'C:/CHKING_2/')
    case 'w':
        playlist_object.streams.get_lowest_resolution().download(r'C:/CHKING_2/')
    case 'a':
        playlist_object.streams.get_audio_only().download(r'C:/CHKING_2/')