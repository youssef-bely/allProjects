from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

# for filename in os.listdir(path):
#     img =Image.open(f"{path}/{filename}")

#     edit = img.filter(ImageFilter.SHARPEN).convert("L")

#     factor = 1.5

#     enhancer = ImageEnhance.Contrast(edit)

#     edit = enhancer.enhance(factor)

#     clean_name = os.path.splitext(filename)[0]

#     edit.save(f'.{pathOut}/{clean_name}_edited.png')


# open the original image
original_img = Image.open(f"{path}/ismail.jpg")

print(f"size : {original_img.size}")
print(f"format : {original_img.format}")
print(f"mode : {original_img.mode}")
# rotating a image 90 deg counter clockwise
#original_img = original_img.rotate(90, Image.NEAREST, expand = 1)



# Flip the original image vertically
vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save(f".{pathOut}/vertical.png")
 
#vertical_img.show()



# Size of the image in pixels
# (size of original image)
# (This is not mandatory)
width, height = original_img.size
 
# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
 
# Cropped image of above dimension
# (It will not change original image)
new_img = original_img.crop((left, top, right, bottom))
newsize = (300, 300)
new_img = new_img.resize(newsize)
new_img.save(f".{pathOut}/ismail_croped.jpg")



# creating a object
vertical_img.load()
 
# Splitting the image into individual
# bands
r, g, b, = vertical_img.split()
 
# merge function used
im1 = Image.merge('RGB', (g, b, r))
im1 = im1.transpose(method=Image.FLIP_TOP_BOTTOM)
im1.save(f".{pathOut}/1.jpg")

# close all our files object
original_img.close()
vertical_img.close()