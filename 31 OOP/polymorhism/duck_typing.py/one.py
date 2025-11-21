# DUCK-TYPPING---If it walks like a duck and quacks like a duck, then just treat it as a duck — no need to check its actual type."
#                 In Python terms:
#                       "An object is suitable if it has the required methods/attributes — we don’t care about its actual class or inheritance."

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive=False
    def speak(self):
        print("HONK!")

animals=[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)


    
# WOOF!
# True
# MEOW!
# True
# HONK!
# False