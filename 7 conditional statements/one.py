#if= do some code if some condition is true
#    else do something else

age=int(input("Enter ur age:"))

if age>=100:
     print("you are too old to sign up")

elif age>=18:
   print("You are eligible to sign up")   

elif age>=0:
    print("you are not born yet")

else:
    print("you must be 18+ to sign up")