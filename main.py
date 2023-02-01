
from fastapi import FastAPI
from model import predict
from pydantic import BaseModel

class Textin(BaseModel):
    state : str
    bankstate : str
    term : int
    noemp : int
    newexist : str
    createjob : int
    retainedjob : int
    franchisecode : str
    urbanrural : str
    revlinecr : str
    lowdoc : str
    grappv : int
    

class Prediction(BaseModel):
    mis_status : bool

app = FastAPI()

@app.post("/predict", response_model=Prediction)
async def root_predict(payload : Textin):
    value = [x for x in payload.__dict__.values()]
    to_return = predict(value)
    return {"mis_status": to_return}