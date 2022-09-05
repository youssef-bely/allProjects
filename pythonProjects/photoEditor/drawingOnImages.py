from PIL import Image, ImageFont, ImageDraw
import math
import os

path = './imgs'
pathOut = '/editedImgs'

stopImg = Image.open(f"{path}/stop.png")

#Adding a Text

watermark_image = stopImg.copy()

# Image is converted into editable form using
# Draw function and assigned to draw
draw = ImageDraw.Draw(watermark_image)

# ("font type",font size)
font = ImageFont.truetype("arial.ttf", 50)

text = u"""\
Youssef
Belemkaddem \n Ismail"""


# Decide the text location, color and font
# (255,255,255)-White color text
draw.text((50, 0), text, (255, 255, 255), font=font)
 
watermark_image.show()

w, h = 500, 300
shape = [(40, 40), (w - 10, h - 10)]
 
# creating new Image object
img = Image.new("RGB", (w, h),(125,125,125))
 
# create line image
img1 = ImageDraw.Draw(img)
#img1.line(shape, fill="none", width=0)
img1.line((0,0,300,200),fill=(255,250,250),width=10)
img1.rectangle((100,100,200,200), fill="#ffff33", outline="red")
side = 8
xy = [
    ((math.cos(th) + 1) * 90,
     (math.sin(th) + 1) * 60)
    for th in [i * (2 * math.pi) / side for i in range(side)]
]

img1.polygon(((200, 200), (300, 100), (250, 50)),fill=(255, 250, 0),outline=(0, 255, 0))
img1.polygon(xy, fill="#eeeeff", outline="blue")
img.show()


