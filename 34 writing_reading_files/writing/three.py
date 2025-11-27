txt_data="I like Pizza!"

employees=["Eugene","squidward","spongebob","patrick"]

file_path="C:\\Users\\Kiran\\OneDrive\\Desktop\\output.txt"

try:
    with open(file_path, 'w') as file:
        for employee in employees:
            file.write(employee +" ")
        print(f"Text file '{file_path}' was created")

except FileExistsError:
    print("This File already exists")
