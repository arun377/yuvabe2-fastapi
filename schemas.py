from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    date:str

class User(BaseModel):
    name:str
    email:str
    password:str    

class Login(BaseModel):
    username:str
    password:str    