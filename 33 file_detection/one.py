# python  file detection----file detection in Python — how to check if a file (or folder) exists, 
#                           is readable, writable, etc., using modern and reliable Python methods.

# this is using relative file path
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



# this is modren amd recommended way to write in 2025

from pathlib import Path
file_path1=Path("Stuff/test.txt")

if file_path1.exists():
    print("path exits")

    if file_path1.is_file():
        print("it's a file")
    elif file_path1.is_dir():
        print("it's a directory")

else:
    print("path doesnt exists")
