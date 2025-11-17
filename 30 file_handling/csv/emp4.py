# read 'n' of employees and data from user,print in empp.csv
import csv

fp=open("empp.csv" ,"w" ,newline="")
csv_object=csv.writer(fp)
# prepare csv header
csv_object.writerow(["eid","ename","esal"])

n=int(input("Enter Number of employees:"))
for i in range(n):
    eid=input("enter Employee ID:")
    ename=input("enter Employee Name:")
    esal=input("enter Employee Salary:")

    csv_object.writerow([eid,ename,esal])

fp.close()