numbers=[1,2,3,4,5,6,7,8,9,10]
def is_odd(number):
    if number%2!=0:
        return True
    else:
        return False

new_odd=list(filter(is_odd,numbers))
print(numbers)                      #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_odd)                      #[1, 3, 5, 7, 9]


#using lambda
numbers=[1,2,3,4,5,6,7,8,9,10]
filter_obj=(lambda n:n%2!=0 ,numbers)
new_odds=list(filter_obj)

print(numbers)                     #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_odds)                    #[1, 3, 5, 7, 9]


print(list(filter(lambda num:num%2!=0 , numbers)))                     #[1, 3, 5, 7, 9]