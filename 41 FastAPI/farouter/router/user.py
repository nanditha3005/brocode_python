from fastapi import APIRouter

router=APIRouter(prefix="/user")

from pydantic import BaseModel

class user(BaseModel):
    uid:int
    uname:str
    email:str
    gender:str
    loc:str

'''
Create
----------------
usage:Create new user
API URL:" http://127.0.0.1:8000/user/create "
Method type:POST
Required fields:uid,uname,email,gender,loc
Access type:public
'''
@router.post('/create')
def create_user():
    return{"msg":"new user created"}



'''
Read user:
-----------------------
usage:read all users
API URL:" http://127.0.0.1:8000/user/"
Method type:GET
Required fileds:None
Access type:public
'''
@router.get("/{uid}")
def fetch_all_users(uid:int):
    return {"msg":"Fetching all users","uid":uid}


'''
update user:
------------
usage:update user by id
API URL:" http://127.0.0.1:8000/user/update/uid"
Method type:PUT
Required fileds:uid,uname,email,gender,loc
Access type:public
'''
@router.put("/update/{uid}")
def update_user(uid:int):
    print(uid)
    return {"msg":"Updated users","uid":uid}


'''
update user:
------------
usage:delete user by id
API URL:" http://127.0.0.1:8000/user/delete/uid"
Method type:DELETE
Required fileds:uid,uname,email,gender,loc
Access type:public
'''

@router.delete("/delete/{uid}")
def delete_user(uid:int):
    print(uid)
    return{"msg":"user deleted succesfully","uid":uid}