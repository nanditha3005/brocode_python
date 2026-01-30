from fastapi import FastAPI
app=FastAPI()

#You are running FastAPI locally on your own computer using uvicorn (the development server).
# uvicorn runs in development mode → it uses HTTP only, not HTTPS.
# HTTPS is disabled by default in local development for speed and simplicity.

'''
usage:home page 
API URL:"http://127.0.0.1:8000/"              
Method type:GET
Required fileds:None
Access type:public
'''
@app.get('/')
def home_page():
    return {"msg":"home page"}


'''
usage:about page 
API URL:"http://127.0.0.1:8000/about"              
Method type:GET
Required fileds:None
Access type:public
'''
@app.get('/about')
def about_page():
    return {"msg":"about page"}


'''
usage:contact page 
API URL:"http://127.0.0.1:8000/contact"              
Method type:GET
Required fileds:None
Access type:public
'''
@app.get('/contact')
def contact_page():
    return {"msg":"contact page"}
