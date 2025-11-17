# r+ === read and write data into file

fp=open("data.txt",'r+')
data=fp.read()
fp.write("Hello,Good Evening")


fp.close()
