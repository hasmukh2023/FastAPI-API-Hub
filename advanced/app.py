from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/login/")
def login(user: User):
    if user.username == "admin" and user.password == "secret":
        return {"message": "Welcome, admin!"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
