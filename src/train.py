from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

def build_model(preprocessor, model_type="rf"):

    if model_type == "rf":
        classifier = RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            class_weight="balanced"
        )

    elif model_type == "logreg":
        classifier = LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )

    pipeline = Pipeline(
        steps=[
            ("preprocessing", preprocessor),
            ("classifier", classifier)
        ]
    )

    return pipeline

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model
