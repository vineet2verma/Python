#  code for single file download by youtube
from asyncio import streams
from pytube import YouTube
import moviepy
from moviepy.editor import *

link = "https://www.youtube.com/watch?v=TEATfq6hPIg" #  youtube link
link = 'https://youtu.be/Q-Io0Y59nYA'
ytube_1 = YouTube(link) # set variable

# print(ytube_1.title) #  for title
# print(ytube_1.thumbnail_url) # for thumbnail


videos = ytube_1.streams.all()  # ALL FILES WITH ALL FORMATS
# videos = ytube_1.streams.filter(only_audio=True) # FILTER AUDIO FILES
# videos = ytube_1.streams.filter(only_video=True) # ALL VIDEO FILES FORMATS
# videos = ytube_1.streams.filter(file_extension="mp4") # ALL VIDEO MP4 FORMATS

# documentation
# ytube_1.streams
    # .filter(only_video=True)  # only video
    # .filter(only_audio = True)  # only audio
    # .order_by("resolution")
    # .desc()
    # .first()
    # .download() 


cont_list = list(enumerate(videos)) # CONVERT TO ENUMERATE LIST
for i in cont_list:
    print (i)
print() # for spacing

strm = int(input("Enter Index No. :- "))
videos[strm].download('C:/CHKING/')
print("Sucessfully Done")

