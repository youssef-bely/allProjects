from pytube import YouTube
####### pip install pytube
from sys import argv
"""
python .\test.py https://www.youtube.com/watch?v=_tXhBLg3Wng
argv[0] => .\test.py
argv[1] => https://www.youtube.com/watch?v=_tXhBLg3Wng
"""

yt = YouTube('https://www.youtube.com/watch?v=_tXhBLg3Wng')

print(yt.title)

print(argv[0])
print(argv[1])


link = argv[1]
yt =YouTube(link)

print("Titre : ", yt.title)
print("Views : ", yt.views)

# Telecharger la video https://www.youtube.com/watch?v=_tXhBLg3Wng

yv = yt.streams.get_highest_resolution()

yv.download('.')

