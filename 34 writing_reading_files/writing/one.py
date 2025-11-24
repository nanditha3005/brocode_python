# python writing files(.txt, .json, .csv)

txt_data="I like pizza!"

file_path="output.txt"

with open(file=file_path, mode="w") as file:
    file.write(txt_data)
    print("txt file '{file_path}' was created")

