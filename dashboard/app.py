import sys
import os
import numpy as np

# Make project root visible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.data_pipeline import prepare_system_data, check_db_connection
from src.clv_engine import compute_clv
from src.cost import get_retention_cost
from src.decision_engine import optimize_budget_clv, optimize_budget_random

st.set_page_config(page_title="Customer Economics Engine", layout="wide")

st.title("Customer Economics Engine")
st.caption("Production-style ML-powered Customer Decision System")

# Health check
db_status = check_db_connection()
if db_status:
    st.success("Database connected successfully.")
else:
    st.error("Database connection failed.")

# Budget control
budget = st.slider("Marketing Budget (₹)", 0, 50000, 10000, step=1000)

# Load REAL data
df = prepare_system_data()

# Compute CLV
df["CLV"] = df.apply(
    lambda x: compute_clv(x["monthly_revenue"], x["churn_prob"]),
    axis=1
)

# Cost
cost_per_customer = get_retention_cost()

# Strategies
clv_selected = optimize_budget_clv(df, budget, cost_per_customer)
random_selected = optimize_budget_random(df, budget, cost_per_customer)

# Profit distributions (simulate uncertainty)
def simulate_profit(selected_ids, n_sim=1000):
    profits = []
    for _ in range(n_sim):
        noise = np.random.normal(1, 0.15)
        profit = df[df["customer_id"].isin(selected_ids)]["CLV"].sum()
        profits.append(profit * noise)
    return np.array(profits)

clv_dist = simulate_profit(clv_selected)
random_dist = simulate_profit(random_selected)

# Stats
clv_mean = clv_dist.mean()
random_mean = random_dist.mean()
improvement_pct = ((clv_mean - random_mean) / random_mean) * 100

# Display table
st.subheader("Customer Table")
st.dataframe(df, use_container_width=True)

# Business decisions
st.subheader("Business Decision")
st.metric("Customers to Retain This Month", len(clv_selected))

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("CLV Strategy Profit (₹)", int(clv_mean))
col2.metric("Random Strategy Profit (₹)", int(random_mean))
col3.metric("Improvement (%)", f"{improvement_pct:.2f}%")

st.info(
    "This system connects directly to a production database, "
    "uses a real ML churn model, and outputs profit-optimized "
    "customer retention decisions."
)
