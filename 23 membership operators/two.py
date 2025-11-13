students={"spongebob","patrick","sandy"}

student=input("Enter the name of a student:")
if student in students:
    print(f"{student} is a student!")
else:
    print(f"{student} was not found")


if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student!")
