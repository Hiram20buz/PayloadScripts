#Extract payload
end_hex=b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
fname=input("Name of the file:")
pname=input("Name of the payload")
with open(fname,'rb') as f:
    content=f.read()
    offset=content.index(end_hex)
    f.seek(offset+len(end_hex))
    
    with open(pname,'wb') as e:
        e.write(f.read())
