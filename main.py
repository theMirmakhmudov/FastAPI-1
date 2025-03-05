from fastapi import FastAPI

app = FastAPI()

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
async def get_model(model_name: ):
    return {"model_name": model_name}