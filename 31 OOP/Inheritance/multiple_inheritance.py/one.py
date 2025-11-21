#  Multiple Inheritance--- inherit from more than one parent class
#                           C(A,B)

#Multilevel inheritance-- inherit from a parent wch inherits from another parent
#                         C(B) <- B(A) <- A


class Prey:
    def flew(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This number is hunting")

class Rabit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabit()
hawk=Hawk()
fish=Fish()

rabbit.flew()              #This number is hunting
# rabbit.hunt()                      bcoz rabbit comes under prey not under predator       
hawk.hunt()                ##This number is eating
fish.flew()                #This number is eating
fish.hunt()                #This number is hunting
