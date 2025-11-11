#itterables==an object/collection that can return its element one at a time
#            allowing it to be iterated over in a loop 

#lists
number=[1,2,3,4,5]
for num in number:
    print(num ,end='-')
print()

numbers=[1,2,3,4,5,6]
for nums in reversed(numbers):
    print(nums ,end=' ')
print()
    

#tuple
number=(1,2,3,4,5)
for num in number:
    print(num ,end='-')
print()

numbers=(1,2,3,4,5,6)
for nums in reversed(numbers):
    print(nums ,end=' ')
print()


#set
fruits={"apple","bannaa","orange","coconut"}
for fruit in fruits:
    print(fruit)
print()


# fruits={"apple","bannaa","orange","coconut"}
# for fruit in reversed(fruits):
#     print(fruit)                      #TypeError: 'set' object is not reversible


#string
name="Bro Code"
for character in name:
    print(character,end="")

print()



#dict
my_dictionary={"A":1 ,"B":2, "C":3}
for key in my_dictionary:
    print(key ,end="\n")
for value in my_dictionary.values():
    print(value)

for key,value in my_dictionary.items():
    print(f"{key}:{value}")