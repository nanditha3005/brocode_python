num=int(input())
factorial=1
for i in range(1,num+1):
    factorial=factorial * i
print(factorial)         #5  120


def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n* factorial(n-1)
    
print(factorial(5))        #120
