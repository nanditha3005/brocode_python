import json
import csv

employees=[["name","age","job"],
           ["spongebob",30,"cook"],
           ["petrick",37,"unemeployed"],
           ["sandy",27,"scientist"]]

file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\output.csv"

try:
    with open(file_path,"w",newline="") as file:
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("That file already exists")