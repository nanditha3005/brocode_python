#Membership operators in Python are used to test whether
#  a value is found in a sequence (like a string, list, tuple, set, or dictionary) or not
#type-- 1.in  -----Returns True if the value is found in the sequence
#       2. not in--Returns True if the value is not found in the sequence

word="APPLE"

letter=input("Guess a letter in secreat word:")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


# if letter not in word:
#     print(f"{letter} was not found")
    
# else:
#     print(f"There is a {letter}")