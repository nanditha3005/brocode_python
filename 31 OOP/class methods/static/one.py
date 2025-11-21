#Static Method = A method that belongs to a class but does NOT need access to the instance (self) or the class (cls).
# It’s just a normal function that lives inside the class for logical grouping.

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        print(f"{self.name}={self.position}")

    @staticmethod
    def is_valid_position(position):
        valid_positions=["Manager","cashier","cook","janitor"]
        return position in valid_positions
    

e1=Employee("rahul","Manager")
e2=Employee("sonia","cashier")
e3=Employee("priyanka","cook")


print(Employee.is_valid_position("cook"))
print(Employee.is_valid_position("Rocket Scientist"))

print(e1.get_info())
print(e2.get_info())
print(e3.get_info())