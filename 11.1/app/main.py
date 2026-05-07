from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Users API")

users_store: dict[int, dict] = {}
next_id = 1


class UserCreate(BaseModel):
    username: str
    email: EmailStr


@app.post("/users", status_code=201)
def register_user(payload: UserCreate):
    global next_id
    user_id = next_id
    next_id += 1
    user = {"id": user_id, "username": payload.username, "email": payload.email}
    users_store[user_id] = user
    return user


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_store.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = users_store.pop(user_id, None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "deleted", "id": user_id}


@app.post("/reset")
def reset_store():
    global next_id
    users_store.clear()
    next_id = 1
    return {"status": "reset"}

