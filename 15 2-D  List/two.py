grocieries=({"apple","orange","banana","coconut"},
             {"celery","carrots","potatoes"},
             {"chicken","fish","turkey"})



# print(grocieries[0])           #['apple', 'orange', 'banana', 'coconut']
# print(grocieries[0][1])        #orange

for collection in grocieries:
    # print(collection) 
    for food in collection:
        print(food,end=" ")    
    print()      