from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username:str
    address:str
    status:str

    class Config:
        orm_mode =True


class UserUpdate(BaseModel):   
    address:str
    status:str
   
    class Config:
        orm_mode =True

class Response(BaseModel):   
    message:str
   