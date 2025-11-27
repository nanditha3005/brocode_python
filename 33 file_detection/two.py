# this is using absolute file path

import os
# file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\test.txt"                #this is for file i.e. create a text document on desktop and cpoy paste the path
file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\test"                      #this is for directory ,i.e. craete a folder on desktop and cpoy paste the path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That loaction doesnt exist")
