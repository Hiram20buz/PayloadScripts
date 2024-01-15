import numpy as np
import PIL.Image


message_to_hide="This is my secret message!"

image=PIL.Image.open('image.png','r')
width,height=image.size
img_arr=np.array(list(image.getdata()))

if image.mode == "P":
    print("Not supported")
    exit()
    
channels= 4 if image.mode == "RGBA" else 3

pixels=img_arr.size // channels
