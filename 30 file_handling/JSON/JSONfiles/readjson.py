# read data form emp.json and print all employee names

import json

fp=open("emp.json","r")
employees=json.load(fp)
print(employees)

# print all employee id
for emp in employees:
    # print(emp['ename'])
    print(emp['eid'])

fp.close()

