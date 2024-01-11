from fastapi import FastAPI
from typing import Optional

app=FastAPI()

@app.get('/')
def index():
    return {'arun':'ak',
            'arjun':'aj'}


@app.get('/blog')
def bl_fun(limit,published:bool=True, sort:Optional[str]=None):
     if published:    
              return {
        "data":f'{limit} blog.these are published ones'
                     }
     else:
           return{
                 "data":f'{limit} blog.these are not published '
           }
     


@app.get('/blog/{id}/comment')
def bl_comment(id):
    return {'comments':{'i used the this product.it is awesome',
                        "worst product.don't waste your money" }}


# @app.get('/blog')
# def bl_fun(id:int):
#     return {
#         "blog no":id
#     }

# @app.get('/about/')
# def index():
#     return {
#         "it is interesting to learn fastapi,it looks like node.js"
#     }

# {
#     "detail": [
#         {
#             "type": "int_parsing",
#             "loc": [
#                 "path",
#                 "id"
#             ],
#             "msg": "Input should be a valid integer, unable to parse string as an integer",
#             "input": "regt",
#             "url": "https://errors.pydantic.dev/2.5/v/int_parsing"
#         }
#     ]
# }