#x:Opens the file for exclusive creation. If the file already exists, an error occurs; otherwise, a new file is created.


#create error message :File ExistError
fp=open('chennai.txt','x')   
fp.write("exclusive creation mode for write operation")    

fp.close()