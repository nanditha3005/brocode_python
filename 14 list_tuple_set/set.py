#set{}-- is unordered and immutable ,but add/remove ok ,but duplicated not allowed 

fruits={"apple","orange","banana","grapes"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))                         #4
# print("pineapple" in fruits)               # False {'banana', 'orange', 'grapes', 'apple'}

#print(fruits[0])                             TypeError: 'set' object is not subscriptable
#fruits.add("pineapple")                       {'apple', 'banana', 'pineapple', 'grapes', 'orange'}
#fruits.remove("apple")                         {'banana', 'grapes', 'orange'}
#fruits.pop()                                   {'orange', 'banana', 'apple'}
fruits.clear()                                  #set()



print(fruits)



enames={101,102,103,104}
print(enames)