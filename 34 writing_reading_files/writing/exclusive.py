txt_data="I like pizza!"

# file_path="output.txt"
file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\output.txt"

try:
    with open(file=file_path,mode="x") as file:
        file.write(txt_data)
        print(f"Text file '{file_path}' was created")

except FileExistsError:
    print("That File already exists")