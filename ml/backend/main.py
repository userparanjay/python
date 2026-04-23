# main.py

from fastapi import FastAPI

import pickle
import numpy as np

# Create FastAPI app
app = FastAPI(title="Placement Prediction API")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))


Request body schema
class StudentData(BaseModel):
    cgpa: float
    iq: float


# Home route
@app.get("/")
def home():
    return {"message": "Placement Prediction API Running"}


# Prediction route
@app.post("/predict")
def predict(data: StudentData):
    
    # Convert input into numpy array
    features = np.array([[data.cgpa, data.iq]])

    # Predict using model
    prediction = model.predict(features)[0]

    # Convert output into readable text
    result = "Placed" if prediction == 1 else "Not Placed"

    return {
        "prediction": int(prediction),
        "result": result
    }