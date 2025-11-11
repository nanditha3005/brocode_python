name="brocode"
age=25
gpa=3.2
is_student=True

print(type(name))          #<class 'str'>
print(type(age))           #<class 'int'>
print(type(gpa))           #<class 'float'>
print(type(is_student))    #<class,'bool'>

gpa=int(gpa)
print(gpa)             #3

age=float(age)
print(age)           #25.0

age=str(age)
print(age)           #25.0
print(type(age))     #<class 'str'>

# age=str(age)
# age+=1     
# print(age)        #TypeError: can only concatenate str (not "int") to str

age=str(age) 
age += "1"     
print(age)       #251

name=bool(name)
print(name)        #true
