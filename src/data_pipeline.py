import pandas as pd
from src.churn_inference import predict_churn_prob

def load_customer_data():
    """
    Load real customer feature data.
    This CSV must match the features used in churn training.
    """
    df = pd.read_csv("data/customers.csv")
    return df

def prepare_system_data():
    """
    Generates system-ready data with real churn probabilities.
    """
    df = load_customer_data()

    # Assume these columns exist in your dataset:
    # ['customer_id', 'monthly_revenue', feature1, feature2, ...]
    feature_cols = [col for col in df.columns 
                    if col not in ["customer_id", "monthly_revenue"]]

    X = df[feature_cols]

    # Real churn probabilities from ML model
    df["churn_prob"] = predict_churn_prob(X)

    return df[["customer_id", "monthly_revenue", "churn_prob"]]
