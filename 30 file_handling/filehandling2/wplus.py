# w+ == open the file for both writing and reading
#        if file already exits then it is overrided /turnicated 
#        if file doesn't exist then new file is created

fp=open("data2.txt","w+")
data=fp.read()
# print(data)

fp.write("My name is aruna")
fp.close()