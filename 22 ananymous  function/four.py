marks=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda m:m+1,marks)))                            #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list(filter(lambda n:n%2!=0 ,marks)))                     #[1, 3, 5, 7, 9]
print(list(filter(lambda n:n%2==0,marks)))                      #[2, 4, 6, 8, 10]

marks=[1,2,3,4,5,6,7,8,9,10]
map_obj=map(lambda m:m+1 ,marks)
new_marks=list(map_obj)
print(marks)
print(new_marks)                                               #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

marks=[1,2,3,4,5,6,7,8,9,10]
filter_obj=filter(lambda m:m%2!=0,marks)
new_marks=list(map_obj)
print(marks)
print(new_marks)   