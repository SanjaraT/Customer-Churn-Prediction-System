import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def load_data(path):
    df = pd.read_csv(path)
    return df

def basic_info(df):
    print("Shape: ", df.shape)
    print("Missing Values :", df.isnull().sum())
    print("Data types: ", df.dtypes)
    print("Target Distribution : ", df["Churn"].value_counts())

def clean_data(df):
    df = df.drop("customerID", axis =1)
    df["TotalCharges"]= pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
    df["SeniorCitizen"] = df["SeniorCitizen"].map({0: "No", 1: "Yes"})
    return df



