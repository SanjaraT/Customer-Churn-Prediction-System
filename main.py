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

    #Models
    print("\nTraining Random Forest...")
    rf_model = build_model(preprocessor, model_type="rf")
    rf_model = train_model(rf_model, X_train, y_train)

    print("\nTraining Logistic Regression...")
    log_model = build_model(preprocessor, model_type="logreg")
    log_model = train_model(log_model, X_train, y_train)

    # Evaluation
    print("Random Forest Evaluation")
    evaluate_model(rf_model, X_test, y_test)

    print("Logistic Regression Evaluation")
    evaluate_model(log_model, X_test, y_test)


    # joblib.dump(model, "model/churn_model.pkl")
    # print("Model saved as churn_model.pkl")

if __name__ == "__main__":
    main()