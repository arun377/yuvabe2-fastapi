from fastapi import APIRouter,Depends
from .. import schemas,database,models
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter(tags=['user'])

@router.get('/user/{id}/')
def getone(id,db:Session=Depends(database.get_db)):
   user=db.query(models.User).filter(models.User.id==id).all()
   return user

pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/user/')
def create(request:schemas.User,db:Session=Depends(database.get_db)):
    hashed_pass=pwd_cxt.hash(request.password)
    new_user =models.User(name=request.name,email=request.email,password=hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {new_user.name,
            new_user.email}