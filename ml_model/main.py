import joblib
from src.EDA import load_data, basic_info, clean_data
from src.Preprocess import split_data, build_preprocessor
from src.train import build_model, train_model
from src.evaluation import evaluate_model, find_best_threshold


def main():
    
    df = load_data("data/churn.csv")
    basic_info(df)
    df = clean_data(df)

    # Split
    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)

    # Preprocessor
    preprocessor = build_preprocessor(X_train)

    #Models
    print("Random Forest")
    rf_model = build_model(preprocessor, model_type="rf")
    rf_model = train_model(rf_model, X_train, y_train)

    print("Logistic Regression")
    log_model = build_model(preprocessor, model_type="logreg")
    log_model = train_model(log_model, X_train, y_train)

    #Threshold tuning 
    print("\nBest threshold for Random Forest")
    rf_best_threshold = find_best_threshold(rf_model, X_val, y_val)

    print("\nBest threshold for Logistic Regression")
    log_best_threshold = find_best_threshold(log_model, X_val, y_val)

    # Evaluation
    evaluate_model(
        rf_model,
        X_test,
        y_test,
        threshold=rf_best_threshold,
        model_name="Random Forest"
    )

    evaluate_model(
        log_model,
        X_test,
        y_test,
        threshold=log_best_threshold,
        model_name="Logistic Regression"
    )


    model_artifacts = {
        "model": log_model,
        "preprocessor": preprocessor,
        "threshold": log_best_threshold
    }

    joblib.dump(model_artifacts, "churn_model.pkl")

    print("\nPipeline and threshold saved as churn.pkl")

    # joblib.dump(log_model, "model/churn_model.pkl")
    # print("\nModel saved as churn_model.pkl")

if __name__ == "__main__":
    main()