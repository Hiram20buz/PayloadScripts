# Hide payload
end_hex=b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

fname=input("Name of the file:")
pname=input("Name of the payload")
with open(fname,'ab') as f, open(pname,'rb') as e:
    f.write(e.read())
  
    
