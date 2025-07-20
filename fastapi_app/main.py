from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi/hello")
def hello():
    return {"message": "Hello from FastAPI!"}
