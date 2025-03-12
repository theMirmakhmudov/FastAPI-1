import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "pdp-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "pdp-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "pdp-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("pdp-", "PDP-")):
        raise ValueError('Invalid ID format, it must start with "pdp-" or "PDP-"')
    return id


@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
