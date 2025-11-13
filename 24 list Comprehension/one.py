double_numbers=[]
for x in range(1,11):
    double_numbers.append(x+1)                 
print(double_numbers)                  #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#using list comprehension
#       [output value  codition expression   condition  ]
doubles=[x+1           for x in range(1,11)              ]
print(doubles)                        #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


triples=[y*3 for y in range(1,11)]
print(triples)                       #[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


squares=[z*z for z in range(1,11)]
print(squares)                       #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]