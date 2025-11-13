fruits=["apple","orange","banana","coconut"]

fruits=[fruit.upper() for fruit in fruits]
print(fruits)                               #['APPLE', 'ORANGE', 'BANANA', 'COCONUT']


fruit_chars=[fruit[0] for fruit in fruits]
print(fruit_chars)                          #['A', 'O', 'B', 'C']

numbers=[1,-2,3,-4,-5,6]
positive_nums=[num for num in numbers  if num>=0]
print(positive_nums)                         #[1, 3, 6]

numbers1=[1,-2,3,-4,-5,6]
negative_nums1=[num for num in numbers1  if num<=0]
print(negative_nums1)                           #[-2, -4, -5]

numbers2=[1,-2,3,-4,-5,6]
even_nums=[num for num in numbers2  if num%2==0]
print(even_nums)                                #[-2, -4, 6]


numbers3=[1,-2,3,-4,-5,6]
odd_nums=[num for num in numbers3  if num%2!=0 ]
print(odd_nums)                                 #[1, 3, -5]

