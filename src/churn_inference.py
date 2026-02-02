import joblib
import pandas as pd

# Load trained churn model
model = joblib.load("models/churn_model.pkl")

def predict_churn_prob(X: pd.DataFrame):
    """
    Returns churn probability for each customer.
    X must contain the same features used in training.
    """
    probs = model.predict_proba(X)[:, 1]
    return probs
