# rawstring== In Python, a raw string is a string literal prefixed with r (or R) that tells Python to 
#              treat backslashes (\) as literal characters instead of escape characters
# 
# Normal string - backslashes are escape characters
print("C:\newfolder\test") 
# Output: C:
#ewfolder        est
# Because \n is interpreted as newline, \t as tab

# Raw string - backslashes are treated literally
print(r"C:\newfolder\test")
# Output: C:\newfolder\test
# Exactly as written!