from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"msg": "Hello from FastAPI"}
