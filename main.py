from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from app import models,schemas
from app.database import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/get_all_users/')
def show_users(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post('/add_user/',response_model=schemas.User)
def create_users(user:schemas.User,db:Session=Depends(get_db)):
    add_user = models.User(username = user.username,address=user.address,status=user.status)
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user

@app.put('/update_user/{user_id}',response_model=schemas.User)
def update_users(user_id:int,user_update:schemas.UserUpdate,db:Session=Depends(get_db)):
    update_user = db.query(models.User).filter_by(id=user_id).first()
    update_user.address=user_update.address
    update_user.status=user_update.status
    db.commit()
    db.refresh(update_user)
    return update_user

@app.delete('/delete_user/{user_id}',response_model=schemas.Response)
def delete_users(user_id:int,db:Session=Depends(get_db)):
    delete_user = db.query(models.User).filter_by(id=user_id).first()
    db.delete(delete_user)
    db.commit()
    response = schemas.Response(message = "Removed successfully")
    return response

