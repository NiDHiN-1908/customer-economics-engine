import os
import psycopg2
import pandas as pd
from src.churn_inference import predict_churn_prob

def load_customer_data():
    """
    Load customer features directly from PostgreSQL.
    Uses environment variables for security.
    """

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "churn_analysis")
    )

    df = pd.read_sql("SELECT * FROM churn_features", conn)
    conn.close()
    return df

def prepare_system_data():
    df = load_customer_data()

    # Split exactly like training
    X = df.drop("churn", axis=1)

    # Real churn probabilities from ML model
    df["churn_prob"] = predict_churn_prob(X)

    # Ensure revenue exists for CLV
    if "monthly_revenue" not in df.columns:
        df["monthly_revenue"] = 1000  # fallback default

    # Ensure customer_id exists
    if "customer_id" not in df.columns:
        df["customer_id"] = df.index.astype(str)

    return df[["customer_id", "monthly_revenue", "churn_prob"]]

def check_db_connection():
    """
    Health check for database connectivity.
    """
    try:
        load_customer_data()
        return True
    except Exception:
        return False
