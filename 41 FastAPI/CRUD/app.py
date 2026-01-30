from fastapi import FastAPI
app=FastAPI()


'''
Usage:Application Root Element
API URL:"http://127.0.0.1:8000/"
Method type:GET
Required fields:None
Access type:Public
'''
@app.get('/')
def home_page():
    return {"msg":"home page"}