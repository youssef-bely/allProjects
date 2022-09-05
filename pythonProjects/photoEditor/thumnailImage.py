from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

stopImg = Image.open(f"{path}/stop.png")
MAX_SIZE = (100, 100)

# Creating the thumbnail
stopImg.thumbnail(MAX_SIZE)
stopImg.save(f".{pathOut}/stop_thumbnail.png")
stopImg.show()