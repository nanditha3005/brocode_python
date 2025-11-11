credit_number="1234-5678-9012-3456"
last_digits=credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")    #xxxx-xxxx-xxxx-3456

credit_number=credit_number[::-1]
print(credit_number)              # reverse 6543-2109-8765-4321