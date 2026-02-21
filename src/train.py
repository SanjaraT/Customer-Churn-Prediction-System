from sklearn.pipeline import Pipeline
from sklearn.ensamble import RandomForestClassifier

def build_model(preprocessor):
    model = Pipeline(
        steps=[
            ("preprocessing", preprocessor),
            ("classifier", RandomForestClassifier(
                n_estimators = 200,
                random_state = 42,
                class_weight = "balanced"
            ))
        ]
    )
    return model

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model
