txt_data="I like Pizza!"

file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\output.txt"



try:
    with open(file_path, 'a') as file:
        file.write("\n"+ txt_data)
        print(f"Text file '{file_path}' was created")


except FileExistsError:
    print("This File already exists")

