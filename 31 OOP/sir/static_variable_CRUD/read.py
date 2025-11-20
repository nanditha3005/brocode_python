#how to read static variable-->  inside a constructor-using classname,self variable
#                                inside a instance method-- using classname
#                                inside class method --using cls and using classname
#                                inside a static method --using classname  
#                                outside a class-using class name and object

class Test():
    a=100

    def m1(self):
        print(Test.a)
        print(self.a)


t1=Test()
print(Test.a)                 #100
print(t1.a)                    #100   #outside a class-using class name and object

t1.m1()