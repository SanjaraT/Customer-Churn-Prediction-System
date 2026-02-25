import joblib 
import pandas as pd
import numpy as np

MODEL_PATH = "model/churn_model.pkl"
MODEL_VERSION = "1.0.0"


loaded_artifacts = joblib.load(MODEL_PATH)

model = loaded_artifacts["model"]
threshold = loaded_artifacts["threshold"]

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    label = "Yes" if prediction == 1 else "No"

    result = {
        "prediction": label,
        "probability": float(np.round(probability, 4)),
        "threshold": threshold,
        "model_version": MODEL_VERSION
    }

    return result