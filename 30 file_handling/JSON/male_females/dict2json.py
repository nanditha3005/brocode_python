import json

fp1=open("emp2.json","r")
fp2=open("user2.json","w")
users=json.load(fp1)

male_Employees=[]
for user in users:
    if user["gender"]=="Male":
        male_Employees.append(user)

print(len(male_Employees))
print(male_Employees)
json.dump("user2.json",fp2)

fp1.close()
fp2.close()