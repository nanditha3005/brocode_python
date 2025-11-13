marks=[1,2,3,4,4,5,6,7,8,9,10]
map_obj=map(lambda m:m+1 ,marks)
new_marks=list(map_obj)
print(marks)
print(new_marks)


marks=[1,2,3,4,4,5,6,7,8,9,10]
filter__obj=filter(lambda n:n%2!=0,marks)
new_mark=list(filter__obj)
print(marks)
print(new_mark)


marks=[1,2,3,4,4,5,6,7,8,9,10]
filter__obj=filter(lambda n:n%2==0 ,marks)
new_mark1=list(filter__obj)
print(marks)
print(new_mark1)