#Hide Secret Messages in PNG Files

end_hex=b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

with open('image.png','ab') as f:
    f.write(b"This is the secret")
    
    
#Get Secret Messages in PNG Files    
''' 
with open('image.png','rb') as f:
    content=f.read()
    offset=content.index(end_hex)
    f.seek(offset+len(end_hex))
    print(f.read())
'''
