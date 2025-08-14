from fastapi import FastAPI
from dataloader import 
app = FastAPI()

@app.get("/data")
def get_data():
    return 