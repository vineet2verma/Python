from email.mime import audio
import py
import pytube
import moviepy
from moviepy.editor import *
from pytube import YouTube

print("YouTube Downlaod Videos")
print('''
1. Audio Downlaod
2. Video Download
3. Both...
''')

option = int(input("Enter The Input :-  "))

def youtube_video():
    print("\n video press \n")
    link = str(input("Enter the Link Here  :  "))
    print()
    yt = YouTube(link)
    video = yt.streams.first()  
    video.download('C:/CHKING/')
    print("\nDownload Completed\n")

def youtube_audio():
    print("\n audio press \n")
    link = str(input("Enter the Link Here  :  "))
    print()
    yt = YouTube(link)
    
    video = yt.streams.first()

    video.download('C:/CHKING/')
    name = yt.title
    file_name = name[0:4]

    mp4 = (f'C:/CHKING/{file_name}.mp4')
    mp3 = (f'C:/CHKING/{file_name}.mp3')

    videocclip2 = VideoClip(mp4+mp3, "C:/CHKING/")
    videocclip2.close()

    VideoClip = VideoFileClip(mp4)
    audioclip = videoclip.audio
    
    audioclip.write_audiofile(mp3)
    audioclip.close()
    videoclip.close()
    print("\nVideo Download Complete\n")

if option == 1:
    youtube_audio()
elif option == 2:
    youtube_video()
elif option == 3:
    youtube_audio()
    youtube_video()
else:
    print("Wrong Input")









