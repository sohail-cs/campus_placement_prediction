import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

#Load the nessary pickle files
with open("model.pkl",'rb')as f:
    lr = pickle.load(f)

with open("columntransformer.pkl",'rb')as pf:
    ct = pickle.load(pf)


with open("labelencoder.pkl",'rb') as lf:
    le = pickle.load(lf)



app = FastAPI()

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
def predict_placement(data : candidate_data):
    input_data = pd.DataFrame([data.model_dump()]) #Convert request from frontend to pandas datafram
    pre_processed_data = ct.transform(input_data) #Preprocess the data
    prediction = lr.predict(pre_processed_data) #Use the trained model to predict
    prediction = le.inverse_transform(prediction) #Convert the numerically encoded prediction back to string

    return {"Placement Predication":prediction[0]} #display the prediction