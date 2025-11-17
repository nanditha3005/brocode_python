#variable scope   ==  where a variable is visible and accessible
#scope resolution ==  is how python finds variable you're reffering to when a name is used
#                     (LEGB) Local-->Enclosed-->Global-->Built-in

def func1():
    a=1
    print(a)

def func2():
    b=2
    print(b)

func1()           #1
func2()           #2