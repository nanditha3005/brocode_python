price1=3.14159
price2=987.45
price3=12.34

print(f"price1 is ${price1:.1f}")           #price1 is $3.1
print(f"price2 is ${price2:.1f}")           #price2 is $-987.5
print(f"price3 is ${price3:.1f}")          #price3 is $12.3

print(f"price1 is ${price1:10}")     #price1 is $   3.14159       
print(f"price2 is ${price2:10}")     #price2 is $   -987.45       
print(f"price3 is ${price3:10}")     #price3 is $     12.34  

print(f"price1 is ${price1:010}")     #price1 is $0003.14159
print(f"price2 is ${price2:010}")     # price2 is $-000987.45  
print(f"price3 is ${price3:010}")     #price3 is $0000012.34


print(f"price1 is ${price1:<10}")     #price1 is $3.14159
print(f"price2 is ${price2:<10}")     #price2 is $-987.45
print(f"price3 is ${price3:<10}")     #price3 is $12.34

print(f"price1 is ${price1:>10}")     #price1 is $   3.14159
print(f"price2 is ${price2:>10}")     # price2 is $   -987.45
print(f"price3 is ${price3:>10}")     #price3 is $     12.34

print(f"price1 is ${price1:+10}")     #price1 is $  +3.14159
print(f"price2 is ${price2:+10}")     #price2 is $   -987.45
print(f"price3 is ${price3:+10}")     #price3 is $    +12.34


print(f"price1 is ${price2:-10}")