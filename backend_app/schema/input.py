from pydantic import BaseModel, Field
from typing import Literal, Annotated


YesNo = Literal["Yes", "No"]
YesNoNoInternet = Literal["Yes", "No", "No internet service"]

class UserInput(BaseModel):
    gender: Literal["Male", "Female"] = Field(description="Customer gender")
    SeniorCitizen: YesNo = Field(description="Whether customer is a senior citizen")
    Partner: YesNo = Field(description="Whether customer has a partner")
    Dependents: YesNo = Field(description="Whether customer has dependents")
    tenure: Annotated[int, Field(ge=0, le=100, description="Number of months the customer has stayed")]

    PhoneService: YesNo = Field(description="Whether customer has phone service")
    MultipleLines: Literal["Yes", "No", "No phone service"] = Field(description="Whether customer has multiple lines")

    InternetService: Literal["DSL", "Fiber optic", "No"] = Field(description="Type of internet service")
    OnlineSecurity: YesNoNoInternet
    OnlineBackup: YesNoNoInternet
    DeviceProtection: YesNoNoInternet
    TechSupport: YesNoNoInternet
    StreamingTV: YesNoNoInternet
    StreamingMovies: YesNoNoInternet

    Contract: Literal["Month-to-month", "One year", "Two year"] = Field(description="Contract type")
    PaperlessBilling: YesNo
    PaymentMethod: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
    MonthlyCharges: Annotated[float, Field(ge=0, description="Monthly subscription charge")]
    TotalCharges: Annotated[float, Field(ge=0, description="Total amount charged to the customer")]

    model_config = {
        "json_schema_extra": {
            "example": {
                "gender": "Male",
                "SeniorCitizen": "No",
                "Partner": "Yes",
                "Dependents": "No",
                "tenure": 12,
                "PhoneService": "Yes",
                "MultipleLines": "No",
                "InternetService": "Fiber optic",
                "OnlineSecurity": "No",
                "OnlineBackup": "Yes",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "Yes",
                "StreamingMovies": "Yes",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 89.5,
                "TotalCharges": 1050.0
            }
        }
    }

class ChurnResponse(BaseModel):
    prediction: int
    probability: float
    threshold: float