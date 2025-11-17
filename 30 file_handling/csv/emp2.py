# read csv file and display all usernames
import csv
fp=open("emp.csv","r")
csv_object=csv.reader(fp)
users=list(csv_object)

for user in users:
#    print(user[1])
#    print(user[2])
   print(user[3])
fp.close()



