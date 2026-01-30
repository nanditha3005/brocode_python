# Taking input from the user
string = input("Enter a string: ")

# Clean the string: remove spaces, convert to lowercase, keep only alphanumeric
cleaned = ''.join(char.lower() for char in string if char.isalnum())

# Check palindrome using slicing
if cleaned == cleaned[::-1]:
    print(f"'{string}' is a palindrome!")
else:
    print(f"'{string}' is not a palindrome.")





def is_palindrome(string):
    # Clean the string
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    
    # Compare with its reverse
    return cleaned == cleaned[::-1]

# Taking input from the user
text = input("Enter a string to check: ")

# Call the function and print result
if is_palindrome(text):
    print(f"'{text}' is a palindrome!")
else:
    print(f"'{text}' is not a palindrome.")