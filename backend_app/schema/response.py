from pydantic import BaseModel

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    threshold: float
    model_version: str