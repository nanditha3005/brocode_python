def divison_check(func):
    def inner(a,b):
        if b==0:
            print("Cant divide by zero")
        else:
            return func(a,b)
    return inner


@divison_check
def subtraction(a,b):
    print(a/b)

subtraction(10,5)         #2.0
subtraction(10,0)         #cant divide by zero
subtraction(200,10)       #20.0