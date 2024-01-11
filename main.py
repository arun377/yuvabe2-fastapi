from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return {'arun':'ak',
            'arjun':'aj'}

@app.get('/blog/{id}')
def bl_fun(id:int):
    return {
        "blog no":id
    }

@app.get('/blog/{id}/comment')
def bl_comment(id):
    return {'comments':{'i used the this product.it is awesome',
                        "worst product.don't waste your money" }}


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