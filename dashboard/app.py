import sys
import os

# Make project root visible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.data_pipeline import load_fake_data
from src.clv_engine import compute_clv
from src.cost import get_retention_cost
from src.decision_engine import optimize_budget

st.set_page_config(page_title="Customer Economics Engine", layout="wide")

st.title("Customer Economics Engine")
st.caption("Optimize customer value. Maximize profit.")

# Budget control
budget = st.slider("Marketing Budget (₹)", 0, 50000, 10000, step=1000)

# Load data
df = load_fake_data()

# Compute CLV
df["CLV"] = df.apply(
    lambda x: compute_clv(x["monthly_revenue"], x["churn_prob"]),
    axis=1
)

# Optimization
cost_per_customer = get_retention_cost()
selected_customers = optimize_budget(df, budget, cost_per_customer)

df["Action"] = df["customer_id"].apply(
    lambda x: "INVEST" if x in selected_customers else "IGNORE"
)

# Display
st.subheader("Customer Decisions")
st.dataframe(df, use_container_width=True)

# Metrics
invest_df = df[df["Action"] == "INVEST"]
total_profit = invest_df["CLV"].sum()
spent_budget = len(invest_df) * cost_per_customer

col1, col2, col3 = st.columns(3)
col1.metric("Customers Selected", len(invest_df))
col2.metric("Budget Spent (₹)", spent_budget)
col3.metric("Expected Profit (₹)", int(total_profit))

st.info(
    "v1 system: budget-constrained optimization using CLV. "
    "Next versions will include discounting, real churn models, and ROI comparison."
)
