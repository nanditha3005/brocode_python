#Enclose scope

def func1():
    x=1

    def func2():
        # x=2
        print(x)
    func2()   

func1()              #1     if x=2 then output is 2