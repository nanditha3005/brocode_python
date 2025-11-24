# @property---decorator used to define a method as a property(it can be accesed like an attribute)
#             Benefit: add additional logic when read,write or delete attributes
#                      gives u getter ,setter and deleter method

class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width =new_width
        else:
            print("Width must be grater than zero")

    @height.setter
    def height(self,new_height):
        if new_height > 0 :
            self._height =new_height
        else:
            print("Height must be grater than zero")

    @width.deleter
    def width(self):
        print("Width has been deleted")

    @height.deleter
    def height(self):
        print("Height has been deleted")

rectangle=Rectangle(3,4)

# rectangle.width=0                            Width must be grater than zero
rectangle.width=5
# rectangle.height=-1                             Height must be grater than zero
rectangle.height=7


print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height