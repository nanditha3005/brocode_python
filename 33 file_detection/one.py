# python  file detection

import os
file_path="stuff/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exits")

    if os.path.isfile(file_path):
        print("That's a file")
    elif os.path.isdir(file_path):
        print("That's a dictonary!")
else:
    print("That location doesn't exist")




