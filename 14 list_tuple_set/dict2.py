user={}
emp={"id":101 ,"name":"rahul","loc":"Wayand" }

print(emp)                    #{'id': 101, 'name': 'rahul', 'loc': 'Wayand'}
print(emp['id'])              #101
print(emp['name'])            #rahul
print(emp['loc'])             #Wayanad
# print(emp['mail'])             #KeyError:'mail

#update
emp1={"id":101 ,"name":"rahul","loc":"wayand" }
emp1['name']="Rahul Gandhi"
print(emp1)                             #{'id': 101, 'name': 'Rahul Gandhi', 'loc': 'wayand'} 

emp1['email']="rahul@123.com"
print(emp1)                              #{'id': 101, 'name': 'Rahul Gandhi', 'loc': 'wayand', 'email': 'rahul@123.com'}