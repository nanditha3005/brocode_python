#while loop- execute some code WHILE some condition remains trrue
#            it is very useful for user input to verify

# name=input("Enter your Name:")
# if name=="":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")


#same program using while loop can be written as

name=input("Enter your name:")

while name=="":
    print("You did not enter your name")
    name=input("Enter your name:")
print(f"Hello {name}")