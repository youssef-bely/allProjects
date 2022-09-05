from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

# open the original image
original_img = Image.open(f"{path}/geek.png")

# Blurring the image
blurImg = original_img.filter(ImageFilter.BLUR)
gaussianBlur = original_img.filter(ImageFilter.GaussianBlur(4))
boxBlur = original_img.filter(ImageFilter.BoxBlur(4))

blurImg.show()
gaussianBlur.show()
boxBlur.show()