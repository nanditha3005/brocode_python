n=int(input("Enter the number (n>=1):"))
if n <=0:
    print("Enter positive number!")
else:
    a,b=0,1
    print("Fibonaccis series")

    for i in range(n):
        print(a,end=" ")
        a,b= b,a+b

    print()


def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10)) 