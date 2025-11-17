import csv
fp=open("emp.csv","r")
csv_object=csv.reader(fp)
user_list=list(csv_object)

for user in user_list:
    print(user)

# print(type(csv_object))                                #<class '_csv.reader'>

fp.close()