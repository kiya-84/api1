from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def javab():
    return "hello world"
