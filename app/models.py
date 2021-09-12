from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(20))
    address = Column(String(200))
    status = Column(String(20))