from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Consumer Attention Mapping System Backend is Running!"}