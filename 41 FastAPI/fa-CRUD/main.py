from fastapi import FastAPI
app=FastAPI()


'''
Usage:Application Root Request
API URL:"http://127.0.0.1:8000/"
Method Type:GET
Required FieldS:None
Access type:Public
'''
@app.get('/')
def home_page():
    return {"msg":"Home page"}



'''
Usage:Application About Request
API URL:"http://127.0.0.1:8000/about"
Method Type:GET
Required FieldS:None
Access type:Public
'''
@app.get("/about")
def about_page():
    return{"message":"About Page"}
users=[
    {'uid':101,'uname':'rahul','gender':'Male'},
    {'uid':102,'uname':'sonia','gender':'Female'},
    {'uid':103,'uname':'priyanka','gender':'Female'},
    {'uid':104,'uname':'modi','gender':'Male'}
]


'''
Usage:Fetch all users
API URL:"http://127.0.0.1:8000/users"
Method Type:GET
Required FieldS:None
Access type:Public
'''
@app.get("/users")
def get_users():
    return {"msg":"all users details","users":users}


'''
Usage:Fetch user by id
API URL:"http://127.0.0.1:8000/users/101"
Method Type:GET
Required FieldS:None
Access type:Public
'''
@app.get("/users/{uid}")
def get_user(uid:int):
    print(uid)
    for user in users:
        if user['uid']==uid:
            return {"user":user}

    return {"msg":"users not exits"}    

# Proper 404 response when user not found
from fastapi import HTTPException
raise HTTPException(status_code=404, detail="User not found")