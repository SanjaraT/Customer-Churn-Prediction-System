import joblib
from src.EDA import load_data, basic_info, clean_data
from src.Preprocess import split_data, build_preprocessor
from src.train import build_model, train_model
from src.evaluation import evaluate_model


def main():
    
    df = load_data("data/churn.csv")
    basic_info(df)
    df = clean_data(df)

    # Split
    X_train, X_test, y_train, y_test = split_data(df)

    # Preprocessor
    preprocessor = build_preprocessor(X_train)

    # Model
    model = build_model(preprocessor)

    # Training
    model = train_model(model, X_train, y_train)

    # Evaluation
    evaluate_model(model, X_test, y_test)

    joblib.dump(model, "model/churn_model.pkl")
    print("Model saved as churn_model.pkl")

if __name__ == "__main__":
    main()