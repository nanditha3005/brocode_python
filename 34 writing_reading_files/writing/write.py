# python writing files(.txt, .json, .csv)

txt_data="I like pizza!"

# file_path="output.txt"
file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\output.txt"

with open(file=file_path,mode="w") as file:
    file.write(txt_data)
    print(f"Text file '{file_path}' was created")