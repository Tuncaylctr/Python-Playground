# fastapi dev main.py
# curl http://localhost:8000

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello World"} 


#fastapi dev main.py
#  curl \-H 'Content-Type: application/json' \ "http://localhost:8000?name=Steve" 
# curl -H 'Content-Type: application/json' 'http://localhost:8000?name=Steve' that one is better 

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def root(name: str = "Alan"):
#     return {"message": f"Hello {name}"}

# # Import date
# from datetime import date

# # Import BaseModel
# from pydantic import BaseModel

# # Define model Item
# class Item(BaseModel):
#     name: str
#     quantity: int = 0
#     expiration: date = None


#fastapi dev main.py
#curl -X POST -H 'Content-Type: application/json' -d '{"name": "bananas"}' http://localhost:8000

# from fastapi import FastAPI
# from pydantic import BaseModel

# # Define model Item
# class Item(BaseModel):
#     name: str

# app = FastAPI()


# @app.post("/")
# def root(item: Item):
#     name = item.name
#     return {"message": f"We have {name}"}


