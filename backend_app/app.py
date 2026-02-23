from fastapi import FastAPI
import joblib

app = FastAPI()

MODEL_PATH = "model/churn.pkl"
MODEL_VERSION = "1.0.0"
model = joblib.load(MODEL_PATH)

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is running"}




@app.get("/health")
def health_check():
    return {
        "status": "OKAY",
        "version": MODEL_VERSION,
        "model_loaded": model is not None
    }