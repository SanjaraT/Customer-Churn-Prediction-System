from fastapi import FastAPI, HTTPException
from model.predict import MODEL_PATH, MODEL_VERSION, model, predict_output
from fastapi.responses import JSONResponse
from schema.input import UserInput

app = FastAPI()

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

@app.post("/predict")
def predict_churn(data: UserInput):

    try:
        # Convert Pydantic model → dict
        user_input = data.model_dump()

        result = predict_output(user_input)

        return JSONResponse(status_code=200, content=result)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )