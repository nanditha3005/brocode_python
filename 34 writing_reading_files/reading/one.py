# python reading files (.txt , .json, .csv)

file_path= "C:\\Users\\Kiran\\OneDrive\\Desktop\\output"

try:
    with open(file_path, "r") as file:
        content=file.read()
        print(content)

except FileNotFoundError:
    print("That file was not found")
