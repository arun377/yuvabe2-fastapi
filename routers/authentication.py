from fastapi import APIRouter,Depends
from .. import schemas,database,models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException, status

pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")

router=APIRouter(tags=['Authentication'])



@router.post('/login')
def login(request:schemas.Login, db:Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No user found')

    if not pwd_cxt.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')

    return user.name; 

# @router.post('/login')
# def login(request:schemas.Login,db:Session=Depends(database.get_db)):
#     user=db.query(models.User).filter(models.User.email==request.username).first()
#     if not user:
#         return 'no user found'
#     elif not pwd_cxt.verify(request.password,user.password):      
#         return 'incorrect password'
#     else:
#         return ('hi '+user.name+'. you successfully logged in.')