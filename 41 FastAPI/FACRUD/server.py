from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
users=[]

class User(BaseModel):
    uid:int
    uname:str
    email:str
    mobile:int

'''
Create
-------------
Usage:Create new user
API URL:"http://127.0.0.1:80000/create"
Method Type:POST
Required Fields:uname,email,mobile
Access type:public
'''
@app.post("/create")
def create_user(user:User):
    print(user)
    users.append(user)
    return{"msg":"New user created","user":user}


'''
read
-------------
Usage:fetch user
API URL:"http://127.0.0.1:80000/read"
Method Type:GET
Required Fields:uname,email,mobile
Access type:public
'''
@app.get('/read')
def get_user():
    return {"msg":"fetch all users"}


'''
update
-------------
Usage:fetch user
API URL:"http://127.0.0.1:80000/update/uid"
Method Type:PUT
Required Fields:uname,email,mobile
Access type:public
'''
@app.put("/update/{uid}")
def update_user(uid:int):
    print(uid)
    return {"msg":"user updated","uid":uid}


'''
delete
-------------
Usage:fetch user
API URL:"http://127.0.0.1:80000/delete/uid"
Method Type:PUT
Required Fields:uname,email,mobile
Access type:public
'''
@app.delete("/delete/{uid}")
def delete_user(uid:int):
    print(uid)
    return {"msg":"user deleted","uid":uid}