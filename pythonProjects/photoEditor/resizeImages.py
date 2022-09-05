from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

# open the original image
original_img = Image.open(f"{path}/ismail.jpg")

# Size of the image in pixels
# (size of original image)
# (This is not mandatory)
width, height = original_img.size
print('image size: ', original_img.size)
print('image width: ', width)
print('image height: ', height)


newsize = (300, 300)
resized_img = original_img.resize(newsize)

resized_img.save(f".{pathOut}/ismail_resized.png")

resized_img.show()
