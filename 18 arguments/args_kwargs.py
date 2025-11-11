#*args(arguments)           =allows you to pass multiple non-key arguments
#**kwargs(keyword arguments)=allows you to pass mutiple keyword arguments
#                             *-->unpacking operator
def add(a,b):
    return a+b

print(add(1,2))    #3

def add(*args):
    print(type(args))              #<class 'tuple'>

add(1,2,3)

def add(*nums):
    total=0
    for num in nums:
        total+=num
    return total

print(add(1,2,3,4,5))            #15
print(add(1))                    #1


def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("Dr.","Spongbob" ,"Harold","Sqaurepants")

#----------------------
#kwargs

def print_address(**kwargs):
    #print(type(**kwargs))            #<class 'dict'>
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_address(street="123",
              apt="100",
              city="detroit",
              state="MI",
              zip="54321")

#-------------------------------------
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg ,end=" ")                   #Dr. Sponebob Sqayrepants III
    print()

    # for value in kwargs.values():
    #     print(value, end=" ")                 #123 100 Detroit MI 54321
   
    print(f"{kwargs.get('street')} {kwargs.get('apt')}")                              #123 fake st.  100
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")          #Detroit MI 54321


shipping_label("Dr.","Sponebob","Sqayrepants","III",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321" )

