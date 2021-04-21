from typing import Optional
from fastapi import FastAPI

# pip install fastapi
# pip install uvicorn
# uvicorn main:app --reload

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
