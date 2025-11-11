#list[]--ordered and changable,duplicates OK
fruits=["apple","banaana","grapes","banaana","orange"]
#print(fruits)

#for fruit in fruits:
    #print(fruit,end=" ")

#print(dir(fruits))                  dir() lists all the attributes and methods of an object.
#print(help(fruits))
#print(len(fruits))                  #4

#fruits[0]='Pineapple'              ['Pineapple', 'banaana', 'grapes', 'orange']
#fruits.append("Pineapple")         ['apple', 'banaana', 'grapes', 'orange', 'Pineapple']
#fruits.remove("orange")            ['apple', 'banaana', 'grapes']
#fruits.insert(2,"pineapple")       ['apple', 'banaana', 'pineapple', 'grapes', 'orange']
#fruits.sort()                      ['apple', 'banaana', 'grapes', 'orange']  
#fruits.reverse()                   ['orange', 'grapes', 'banaana', 'apple']
#fruits.clear()                         []
#print(fruits.index("apple"))           0
#print(fruits.index("orange"))          3
#print(fruits.index("pineapple"))       # ValueError: 'pineapple' is not in list
#print(fruits.count("apple"))            #1
print(set(fruits))                       #removes dupliactes in a list


print(fruits)                
