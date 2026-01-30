# number=int(input())
# factorial =1
# for i in range(1,number +1):
#     factorial =factorial *i
# print(factorial)


# num=int(input())
# num2=input()

# print (num *num2)


def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))