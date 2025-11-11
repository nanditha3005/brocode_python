unit=input("Is this temparature in Celsius or Fahrenheit (C/F):")
temp=float(input("Enter the temparature:"))

if unit=="C":
    temp=((9* temp)/5 +32, 1)
    print(f"The temparature in fareheite is{temp}°F")
elif unit =="F":
    temp=round((temp-32)* 5/9 , 1)
    print(f"The temparature in Celcius is{temp}°C")
else:
    print(f"{unit} is a invalid unit measurement")