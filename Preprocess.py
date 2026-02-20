from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def split_data(df):
    X = df.drop("Churn", axis=1)
    y = df["Churn"].map({"No":0, "Yes":1})

    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def build_preprocessor(X):
    cat_cols = X.select_dtypes(include=["object"]).columns
    num_cols = X.select_dtypes(include=["int64","float64"]).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(),num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"),cat_cols)
        ]
    )
    return preprocessor