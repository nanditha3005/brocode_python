#withot function
marks=[35,36,37,38,39]

new_marks=[]
for mark in marks:
    new_marks.append(mark+1)

print(marks)                      #[35, 36, 37, 38, 39]
print(new_marks)                  #[36, 37, 38, 39, 40]



#with function
mark=[35,36,37,38,39]
new_mark=[]
def add_mark(mark):
    return mark+1
for marks in mark:
    new_mark.append(add_mark(marks))

print(mark)                               #[35, 36, 37, 38, 39]
print(new_mark)                           #[36, 37, 38, 39, 40] 



#using map
marks=[35,36,37,38,39]
def add_marks(mark):
    return mark+1

map_obj=map(add_mark,marks)
new_marks=list(map_obj)
print(marks)                                #[35, 36, 37, 38, 39]
print(new_marks)                             #[36, 37, 38, 39, 40] 



#using lambda
marks=[35,36,37,38,38,39]
map_obj=map(lambda m:m+1 ,marks)
new_marks=list(map_obj)

print(marks)                                       #[35, 36, 37, 38, 39]       
print(new_marks)                                 #[36, 37, 38, 39, 40]


#print(list(map(lambda mark:mark+1 ,marks)))          #[36, 37, 38, 39, 40] 