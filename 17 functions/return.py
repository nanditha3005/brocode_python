def add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z


print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

#using return statement
def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first +" "+ last

full_name=create_name("spongebob","squarepants")

print(full_name)