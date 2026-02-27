**Project Overview**

A full-stack Machine Learning application that predicts customer churn using the Telco Customer Churn dataset, deployed with a FastAPI backend and Streamlit frontend. This project implements an end-to-end Machine Learning pipeline for predicting whether a telecom customer is likely to churn.

The system includes:

- Data preprocessing pipeline

- Model training and threshold tuning

-  REST API using FastAPI

- Interactive frontend using Streamlit

- Full separation of training and inference environments

**Dataset**

* Dataset: Telco Customer Churn
* Source: Kaggle
* Target Variable: Churn

The dataset contains customer information including:

- Demographics (gender, senior citizen, dependents)

- Account information (tenure, contract type, payment method)

- Services subscribed (internet, streaming, tech support)

- Billing details (monthly charges, total charges)

**ML Pipeline**

Built a stratified 70/15/15 train-validation-test pipeline with OneHotEncoding for categorical features and StandardScaler for numerical features. Trained Logistic Regression and Random Forest models using Scikit-learn pipelines. Performed threshold tuning on the validation set to optimize F1-score. Deployed a Logistic Regression model with balanced class weights and a tuned probability threshold, saved along with the full preprocessing pipeline using joblib.

**Backend (FastAPI)**

Built a REST API using FastAPI to serve the trained churn model.
Implemented:

- /predict endpoint to process customer features and return predictions

- /health endpoint for model status monitoring

- Pydantic schema validation with field normalization

- predict_output() function for inference and threshold-based classification

The API returns Yes/No prediction, probability score, threshold value, and model version while ensuring consistent preprocessing during inference.

**Frontend (Streamlit)**

Developed an interactive Streamlit UI that:

- Collects user inputs through structured form components

- Uses get_prediction() to send POST requests to the backend

- Displays prediction results with probability insights

- Provides real-time feedback and error handling

The frontend ensures seamless communication between user input and backend inference.

**Technologies Used**

- Python

- Scikit-learn

- FastAPI

- Streamlit

- Pydantic

- Pandas

- NumPy

- Joblib

**Author**
### Sanjara