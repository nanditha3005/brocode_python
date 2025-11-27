import json

employee={
    "name":"spongebob",
    "age":30,
    "job":"cook"
}

file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\output.json"

try:
    with open(file_path ,"w") as file:
        json.dump(employee ,file , indent=4)
        print(f"JSON file '{file_path}' was created")

except FileExistsError:
    print("That file alrwady exists")