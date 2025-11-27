import csv
from pathlib import Path

file_path=Path("C:\\Users\\Kiran\\OneDrive\\Desktop\\output.csv")

try:
    with open(file_path,"r") as file:
        content=csv.reader(file)
        for line in content:
            print(line[2])

except FileNotFoundError:
    print("That file was not found")