from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

def build_model(preprocessor):
    model = Pipeline(
        steps=[
            ("preprocessing", preprocessor),
            ("classifier", RandomForestClassifier(
                    n_estimators=400,
                    max_depth=10,
                    min_samples_split=5,
                    class_weight="balanced_subsample"
                ))
        ]
    )
    return model

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model
