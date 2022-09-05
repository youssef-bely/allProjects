""" ImageEnhance.Color() is used to adjust the color balance of an image, in a manner similar to the controls on a color TV set. 
An enhancement factor of 0.0 gives a black and white image. A factor of 1.0 gives the original image. """

# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance

import os

path = './imgs'
pathOut = '/editedImgs'

# Opening Image
im = Image.open(f"{path}/ismail.jpg")
 
# Creating object of Color class
im3 = ImageEnhance.Color(im)
 
# showing resultant image
im3.enhance(5.0).show()

# Creating object of Contrast class
im3 = ImageEnhance.Contrast(im)
 
# showing resultant image
im3.enhance(5.0).show()

# Creating object of Brightness class
im3 = ImageEnhance.Brightness(im)
 
# showing resultant image
im3.enhance(1.5).show()

# Creating object of Sharpness class
im3 = ImageEnhance.Sharpness(im)
 
# showing resultant image
im3.enhance(5.0).show()


