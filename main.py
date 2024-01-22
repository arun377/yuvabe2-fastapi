from fastapi import FastAPI,Depends,Query
from . import schemas,models
from .database import engine,get_db
from sqlalchemy.orm import Session
# from passlib.context import CryptContext
from .routers import blog,authentication
from fastapi.middleware.cors import CORSMiddleware

  
app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)


# def get_db():
#     db=SessionLocal()

#     try:
#         yield db
#     finally:
#         db.close()



@app.post('/blog/',tags=['blogs'])
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog =models.Blog(title=request.title,body=request.body,date=request.date)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog/',tags=['blogs'])
def all(db:Session=Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blog/{date}', tags=['date'])
def get_blogs(date, db: Session = Depends(get_db)):
    if date:
        # Perform filtering based on the provided date
        blogs = db.query(models.Blog).filter(models.Blog.date == date).all()
    else:
        # Return all blogs if no date is provided
        blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}/',tags=['blogs'])
def getone(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).all()
    return blog

@app.put('/blog/{id}/',tags=['blogs'])
def update(id,request:schemas.Blog,db:Session=Depends(get_db)): 
    db.query(models.Blog).filter(models.Blog.id==id).update(request)
                                                           
    db.commit()
    return 'updated'
    

@app.delete('/blog/{id}',tags=['blogs'])
def remove(id,db:Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)     
    db.commit()
    return f'done.{id} got deleted'

# pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post('/user',tags=['user'])
# def create(request:schemas.User,db:Session=Depends(get_db)):
#     hashed_pass=pwd_cxt.hash(request.password)
#     new_user =models.User(name=request.name,email=request.email,password=hashed_pass)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {new_user.name,
#             new_user.email}

# @app.get('/user/{id}',tags=['user'])
# def getone(id,db:Session=Depends(get_db)):
#    user=db.query(models.User).filter(models.User.id==id).all()
#    return user


    # return {'got it',
    #         f'Title:{request.tit}',
    #          f'Body:{request.bdy}'
    #        }       

