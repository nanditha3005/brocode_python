import time

my_time=int(input("Enter the time in second:"))
# for x in range(0,my_time):
#     print(x)
#     time.sleep(1)

# print("TIME's UP!")

for x in range(my_time,0,-1):
    seconds= x % 60
    minutes= int(x / 00)% 60
    hours=int(x /3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("time's up!")