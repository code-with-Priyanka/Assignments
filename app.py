from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

data_store = {}

class Students(BaseModel):
    name: str
    registration_no: int
    # course_id: int
    # course_name: str

@app.get("/")
def get_data():
    return {
         "name":data_store
    }

@app.post("/add")
def post_data(body: Students):
    data_store[body.registration_no] = body.name
    return body

@app.put("/update/{registration_no}")
def update_data(registration_no: int, body: Students):
    
    data_store[registration_no] = body.name
    return data_store

@app.delete("/delete/{registration_no}")
def delete_data(registration_no: int, body: Students):
    del data_store[registration_no]
    return data_store

    
    
    

