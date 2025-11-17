fp=open("one.txt",'w')

print(fp.name)               #one.txt
print(fp.mode)               #w
print(fp.readable())         #False
print(fp.writable())         #True

fp.close()
print(fp.closed)             #True
