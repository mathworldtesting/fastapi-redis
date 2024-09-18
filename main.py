from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "welcome to the API" }

@app.get("/random")
def random_number():
    return {"random number": random.randint(0, 12)}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)