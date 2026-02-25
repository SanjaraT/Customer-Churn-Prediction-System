import numpy as np
from sklearn.metrics import classification_report, roc_curve, confusion_matrix, roc_auc_score


def apply_threshold(y_prob, threshold=0.5):
    return (y_prob >= threshold).astype(int)


def find_best_threshold(model, X_val, y_val):
    y_prob = model.predict_proba(X_val)[:, 1]

    fpr, tpr, thresholds = roc_curve(y_val, y_prob)

    optimal_idx = (tpr - fpr).argmax()
    optimal_threshold = thresholds[optimal_idx]

    print(f"Best threshold found: {optimal_threshold:.4f}")

    return optimal_threshold


def evaluate_model(model, X, y, threshold=0.5, model_name="Model"):
    y_prob = model.predict_proba(X)[:, 1]
    y_pred = apply_threshold(y_prob, threshold)

    print(f"\n{model_name} Evaluation (Threshold={threshold:.2f})")

    print("Confusion Matrix:")
    print(confusion_matrix(y, y_pred))

    print("\nClassification Report:")
    print(classification_report(y, y_pred))

    print("ROC-AUC Score:", roc_auc_score(y, y_prob))
# from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# def evaluate_model(model, X_test, y_test):
#     y_pred = model.predict(X_test)
#     y_prob = model.predict_proba(X_test)[:, 1]

#     print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
#     print("Classification Report:\n", classification_report(y_test, y_pred))
#     print("ROC-AUC Score:", roc_auc_score(y_test, y_prob))
