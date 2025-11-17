#Global scope

def func1():
    print(x)

def func2():
    print(x)

x=3
# x=4               if x is not commented then it x=4 would override x=3 and prints x=4


func1()                  #3
func2()                  #3