import joblib 
import pandas as pd
import numpy as np

MODEL_PATH = "model/churn.pkl"
MODEL_VERSION = "1.0.0"

model = joblib.load(MODEL_PATH)

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    threshold = 0.5

    result = {
        "prediction": int(prediction),
        "probability": float(np.round(probability, 4)),
        "threshold": threshold,
        "model_version": MODEL_VERSION
    }

    return result