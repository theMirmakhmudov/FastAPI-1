from typing import Annotated

from fastapi import FastAPI, Query
from models2 import Item

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

@app.get("/items/")
async def read_item(q: Annotated[str | None, Query(max_length=3)]):
    results = {"item": [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/array/")
async def read_item(q: Annotated[list[str] | None, Query()] = None):
    query_items = {
        "q": q
    }
    return query_items