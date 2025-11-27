import datetime

date = datetime.date(2025,1,2)        #(year,month,date)
today= datetime.date.today()

time=datetime.time(12,30,0)                  #(hour,minute,second)
now=datetime.datetime.now()

now= now.strftime(f"%H:%M:%S  %m-%d-%Y")

target_datetime= datetime.datetime(2030,1,2 ,12,30,0)
current_datetime=datetime.datetime.now()
if target_datetime < current_datetime:
    print("Target date has passed ")
else:
    print("Target date has not passed")


print(today)
print(date)
print(time)
print(now)
