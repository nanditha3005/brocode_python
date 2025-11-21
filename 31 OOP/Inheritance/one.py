# Inheritance--- allows a class to inherit attribute and methods from anothe class
#                help with code reusability and extensibility
#                class Child(Parent)

class Animal:

    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQEEK!")

dog=Dog("Scuby")
cat=Cat("Garfield")
mouse=Mouse("Mickey")



print(dog.name)                 #Scuby
print(dog.is_alive)             #True
dog.eat()                       #Scuby is eating
dog.sleep()                     #Scuby is sleeping

dog.speak()                     #WOOF!
cat.speak()                     #MEOW!
mouse.speak()                   #SQEEK!


