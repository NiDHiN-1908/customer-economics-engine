import pandas as pd

def load_fake_data():
    data = {
        "customer_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "monthly_revenue": [1200, 800, 300, 1500, 400, 900, 2000, 600],
        "churn_prob": [0.1, 0.3, 0.6, 0.05, 0.4, 0.2, 0.08, 0.5]
    }
    return pd.DataFrame(data)
