from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# define model Item
class Item(BaseModel):
    name: str
    quantity: Optional[int] = 0

app = FastAPI()

items = {}


@app.post("/items")
def create(item: Item):
    name = item.name
    if name in items:
        raise HTTPException(status_code=409, detail="Item exists")
    items[name] = item
    return {"message": f"Added {name} to items."}
  
@app.get("/items")
def read(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[name]  
  
@app.put("/items")
def update(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[name] = item
    return {"message": f"Updated {name}."}
  
@app.delete("/items")
def delete(item: Item):
    name = item.name
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[name]
    return {"message": f"Deleted {name}."}


#fastapi dev main.py
# curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{"name": "rock"}' \
  http://localhost:8000/items

curl http://localhost:8000/items?name=rock

curl -X PUT \
  -H 'Content-Type: application/json' \
  -d '{"name": "rock", "quantity": 100}' \
  http://localhost:8000/items

curl -X DELETE \
  -H 'Content-Type: application/json' \
  -d '{"name": "rock"}' \
  http://localhost:8000/items

curl http://localhost:8000/items?name=rock


#functional test



import requests

ENDPOINT = "http://localhost:8000/items"

# Create item "rock" without providing quantity
r = requests.post(ENDPOINT, json={"name": "rock"})
assert r.status_code == 200
assert r.json()["message"] == "Added rock to items."

# Verify that item "rock" has quantity 0
r = requests.get(ENDPOINT + "?quantity=0")
assert r.status_code == 200
assert r.json()["quantity"] == 0

# Update item "rock" with quantity 100
r = requests.put(ENDPOINT, json={"name": "rock", "quantity": 100})
assert r.status_code == 200
assert r.json()["message"] == "Updated rock."

# Verify that item "rock" has quantity 100
r = requests.get(ENDPOINT + "?name=rock")
assert r.status_code == 200
assert r.json()["quantity"] == 100

# Delete item "rock"
r = requests.delete(ENDPOINT, json={"name": "rock"})
assert r.status_code == 200
assert r.json()["message"] == "Deleted rock."

# Verify that item "rock" does not exist
r = requests.get(ENDPOINT + "?name=rock")
assert r.status_code == 404

print("Test complete.")