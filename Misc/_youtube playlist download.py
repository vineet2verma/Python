#  playlist download code
import py
from pytube import Playlist

link = "https://www.youtube.com/playlist?list=PLjVLYmrlmjGeoNFWriOghLF9BPJkixMMj"
# link = "https://youtu.be/KlWOr2RwqM4?list=PL0b6OzIxLPbzf12lu5etX_vjN-eUxgxnr"
py = Playlist(link)
py_title = py.title
py_urls = py.video_urls

# print(py_urls)


# print(py.title)  
# print(f'Downloading : {py.title}\n {py.video_urls}' )

for i,video in enumerate(py.videos):
    print( f'title {i+1} :-  {video.title}' )


    