# MODULE== a file containing code you want to include in your program
#          use 'import' to include a module(built in or your own)
#          useful to break up a large program reuable separte files.

# print=help("modules")
# print=help("dir")


import math 
print(math.pi)                          #3.141592653589793

import math as m
print(m.pi)                             #3.141592653589793

from math import e
a,b,c,d,e=1,2,3,4,5


print(e ** a)              #5
print(e ** b)              #25
print(e ** c)              #125
print(e ** d)              #625
print(e ** e)              #3125


print(math.e ** a)         #2.718281828459045
print(math.e ** b)         #7.3890560989306495
print(math.e **c)          #20.085536923187664
print(math.e ** d)         #54.59815003314423
print(math.e ** e)         #148.41315910257657


