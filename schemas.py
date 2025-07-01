from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    body: str
    user_id: int
    
class BlogBase(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True

class BlogUpdate(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name:str
    email:str
    password:str

class showUser(BaseModel):
    name:str
    email:str
    blogs:List[BlogBase] = []
    class Config():
        orm_mode = True

class showUserInBlog(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True

class showBlog(BaseModel):
    title: str
    body: str 
    creator: showUserInBlog
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None 
