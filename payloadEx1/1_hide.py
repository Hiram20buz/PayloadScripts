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

stop_indicator="$NEURAL$"
stop_indicator_length=len(stop_indicator)

message_to_hide += stop_indicator

byte_message =''.join(f"{ord(c):08b}" for c in message_to_hide)

print(byte_message)
