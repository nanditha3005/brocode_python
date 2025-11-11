#validate user input exercise
#1.username is no more than 12 characters  --len(username) >12
#2.username must not contain spaces     -----username.find("")
#3.username must not contain digits     -----username.isalpha()

username= input("Enter a username:")

if len(username) >12:
    print("Your username can't be more than 12 characters")
elif " " in username:
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("your usersname can't contain digits")

else:
    
    print(f"Welcome {username}")