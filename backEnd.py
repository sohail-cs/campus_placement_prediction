from fastapi import FastApi
from pydantic import BaseModel


app = FastApi()

class candidate_data(BaseModel):
    gender: str
    ssc_p: float
    ssc_b: str
    hsc_p: float
    hsc_b: str
    hsc_s: str
    degree_p: float
    degree_t: str
    workex: str
    etest_p: float
    specialisation: str
    mba_p: float


@app.post("/")
def predict_placement():
    