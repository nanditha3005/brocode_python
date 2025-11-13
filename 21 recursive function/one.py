def factorial(n):
    #Base Case
    if n==0 or n==1:
        return 1
    #recursive case
    else:
        return n* factorial(n-1)
    
print(factorial(5))


#output
# factorial(5) → 5 * factorial(4)
#                5 * (4 * factorial(3))
#                5 * (4 * (3 * factorial(2)))
#                5 * (4 * (3 * (2 * factorial(1))))
#                5 * (4 * (3 * (2 * 1))) → 120