import joblib
import pandas as pd

# Load trained churn model (from models/ folder)
model = joblib.load("models/churn_model.pkl")

def predict_churn_prob(X: pd.DataFrame):
    """
    Returns churn probability for each customer.
    X must match the features used in training.
    """
    probs = model.predict_proba(X)[:, 1]
    return probs
