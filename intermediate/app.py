from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
def greet(name: str, age: int = None):
    message = f"Hello, {name}!"
    if age:
        message += f" You are {age} years old."
    return {"message": message}
