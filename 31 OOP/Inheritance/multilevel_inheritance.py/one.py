#Multilevel inheritance-- inherit from a parent wch inherits from another parent
#                         C(B) <- B(A) <- A

class Animal:
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print(f" {self.name} is eating")

    def sleep(self):
        print(f" {self.name} is sleeping")

class Prey(Animal):
    def flew(self):
        print(f" {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f" {self.name} is hunting")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabit("Bugs")
hawk=Hawk("Tony")
fish=Fish("Nemo")

rabbit.eat()            #This Bugs is eating
rabbit.sleep()          #This Bugs is sleeping
hawk.eat()              #This Tony is eating
hawk.sleep()            #This Tony is sleeping
fish.eat()              #This Nemo is eating
fish.sleep()            #This Nemo is sleeping


rabbit.eat()
rabbit.sleep()
rabbit.flew()
# rabbit.hunt()      #is not possible

hawk.eat()
hawk.sleep()
# hawk.flew()         #not possible
hawk.hunt()

fish.eat()
fish.sleep()
fish.flew()
fish.hunt()