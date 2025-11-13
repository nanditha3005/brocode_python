grades={"Sandy":"A","Squidward":"B","Spongebob":"C","Petrick":"D"}

student=input("Enter the name of student:")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")