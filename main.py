from fastapi import FastAPI
from models import Users

app = FastAPI()

video_db = {}

testdb = [
    {
        "item_name": "Foo1"
    },
    {
        "item_name": "Foo2"
    },
    {
        "item_name": "Foo3"
    },
    {
        "item_name": "Foo4"
    },
    {
        "item_name": "Foo5"
    }
]


@app.get('/')
async def root():
    return {'message': 'Welcome to the FastAPI API!'}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/user/me")
async def get_user_me():
    return {"user": "Current the user"}


@app.get("/users")
async def get_users():
    return [{"user_id": i, "username": f"user{i}"} for i in range(1, 6)]


@app.get("/models/{model_name}")
async def get_model(model_name: Users):
    return {"model_name": model_name}


@app.post("/api/user/{video_id}/like")
async def like_video(video_id: int):
    if video_id not in video_db:
        video_db[video_id] = {"likes": 0, "views": 0}

    video_db[video_id]["likes"] += 1

    return {
        "message": "Video yoqdi",
        "video_id": video_id,
        "total_likes": video_db[video_id]["likes"]
    }


@app.post("/api/user/{video_id}/viewer")
async def view_video(video_id: int):
    if video_id not in video_db:
        video_db[video_id] = {"likes": 0, "views": 0}

    video_db[video_id]["views"] += 1

    return {
        "message": "Video ko'rildi",
        "video_id": video_id,
        "total_views": video_db[video_id]["views"]
    }


@app.get("/items")
async def read_items(skip: int = 0, limit: int = 4):
    return testdb[skip: skip + limit]
