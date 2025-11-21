# super() --> Function used in a child class to call methods from parent class(superclass)
#             Allows to extend the functionality of inherited methods


class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled' }")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        # self.color=color
        # self.filled=filled
        super().__init__(color,is_filled)
        self.radius=radius
    
    def describe(self):    
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")    #(child)circle describe overrides the (parent)shape decribe, so we use super to solve the overridding
        super().describe()    


class Square(Shape):
    def __init__(self,color,is_filled,width):
        # self.color=color
        # self.filled=filled
        super().__init__(color,is_filled)
        self.width=width

    def describe(self):
        print(f"It is a square with an area of { self.width * self.width}")
        super().describe()


class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        # self.color=color
        # self.filled=filled
        super().__init__(color,is_filled)
        self.width=width
        self.height=height

    def describe(self):
        print(f"It is a triangle with an area of { self.width * self.height /2} cm^2")
        super().describe()


circle=Circle(color="red",is_filled=True,radius=5)
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

print("------------------")

square=Square(color="blue", is_filled=False,width=6)
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")

print("------------------")

triangle=Triangle(color="green",is_filled=True ,width=6,height=8)
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

print("------------------")

circle.describe()
square.describe()
triangle.describe()