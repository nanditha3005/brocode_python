#A=P(1+r/n)power t

principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter the principle amount:"))
    if principle <=0:
        print("principle cant be less than or equal to zero")

while rate<=0:
    rate=float(input("Enter the interest rate:"))
    if rate <=0:
        print("Interest rate cant be less than or equal to zero")

while time<=0:
    time=float(input("Enter the time in years:"))
    if time <=0:
        print("time cant be less than or equal to zero")

total=principle* pow((1 +rate/100),time)
print(f"Balance after {time}year/s:${total:.2f}")    #Enter the principle amount:1000
                                                     #Enter the interest rate:10
                                                     #Enter the time in years:1
                                                     #Balance after 1.0year/s:$1100.00



