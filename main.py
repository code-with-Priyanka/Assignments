from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Friends"}

@app.get("/about")
async def about():
    return {"message": "I am Priyanka working as an intern in Knowlwdge Lens"}
