# 1. Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):              # Single inheritance
    def bark(self):
        print("Woof!")


a1=Animal()
a2=Dog()
a2.speak()
a2.bark()
