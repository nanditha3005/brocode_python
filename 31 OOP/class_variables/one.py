# class variables--- shared among all instances of a class
#                    defined outside a constructor
#                    allow you to share data among all objects created from that class

class student:
    
    class_year=2025
    num_students=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.num_students += 1


student1=student("rahul",45)     
student2=student("sonia",34)
student3=student("priyanka",23)

print(student1.name)                  #rahul
print(student1.age)                   #45
print(student2.name)                  #sonia
print(student2.age)                   #34
print(student1.class_year)            #2025
print(student2.class_year)            #2025
print(student.class_year)             #2025  its better to create a class variable using class name rather than using objects

print(student.num_students)            #3

print(f"My graduating class of {student.class_year} has {student.num_students} students")                  #My graduating class of 2025 has 3 students
print(student1.name)                  #rahul
print(student2.name)                  #sonia
print(student3.name)                  #priyanka
