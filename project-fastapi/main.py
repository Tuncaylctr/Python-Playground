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


# #fastapi dev main.py
# #curl -X PUT -H 'Content-Type: application/json' -d '{"name": "bananas", "description": "Delicious!"}' http://localhost:8000/items

# from fastapi import FastAPI
# from pydantic import BaseModel

# # Define model Item
# class Item(BaseModel):
#     name: str
#     description: str

# # Define items at application start
# items = {"bananas": "Yellow fruit."}

# app = FastAPI()


# @app.put("/items")
# def update_item(item: Item):
#     name = item.name
#     # Update the description
#     items[name] = item.description
#     return item



# #fastapi dev main.py
# # curl -X DELETE -H 'Content-Type: application/json' -d '{"name": "bananas"}' http://localhost:8000/items

# from fastapi import FastAPI
# from pydantic import BaseModel

# # Define model Item
# class Item(BaseModel):
#     name: str  #

# # Define items at application start
# items = {"apples", "oranges", "bananas"}

# app = FastAPI()

# @app.delete("/items")
# def delete_item(item: Item):
#     name = item.name
#     # Delete the item
#     items.remove(name)  
#     return {}           



# #fastapi dev main.py
# # curl -X DELETE  -H 'Content-Type: application/json' -d '{"name": "bananas"}' http://localhost:8000/items

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# # Define moel Item
# class Item(BaseModel):
#     name: str

# # Define items at application startup
# items = {"apples", "oranges"}

# app = FastAPI()


# @app.delete("/items")
# def delete_item(item: Item):
#     name = item.name
#     if name in items:
#         items.remove(name)
#     else:
#         # Raise HTTPException with status code for "not found"
#         raise HTTPException(status_code=404, detail="Item not found.")
#     return {}


# #fastapi dev main.py
# #curl -X DELETE -H 'Content-Type: application/json'  -d '{"name": "rock"}' http://localhost:8000/items curl -X DELETE -H 'Content-Type: application/json' -d '{"name": "roll"}' http://localhost:8000/items
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# # Define model Item
# class Item(BaseModel):
#     name: str

# app = FastAPI()

# items = {"rock", "paper", "scissors"}


# @app.delete("/items")
# # Make asynchronous
# async def root(item: Item):
#     name = item.name
#     # Check if name is in items
#     if name not in items:
#         # Return the status code for not found
#         raise HTTPException(status_code=404, detail="Item not found.")
#     items.remove(name)
#     return {"message": "Item deleted"}

