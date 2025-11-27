import json
from pathlib import Path
file_path=Path("C:Users\\Kiran\\OneDrive\\Desktop\\output.json")

try:
    with open(file_path, "r") as file:
        content=json.load(file)
        print(content)

except FileNotFoundError:
    print("That file was not found")
