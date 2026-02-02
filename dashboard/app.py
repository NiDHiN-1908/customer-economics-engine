import sys
import os

# Make project root visible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.data_pipeline import load_fake_data
from src.clv_engine import compute_clv
from src.cost import get_retention_cost
from src.decision_engine import optimize_budget_clv, optimize_budget_random

st.set_page_config(page_title="Customer Economics Engine", layout="wide")

st.title("Customer Economics Engine")
st.caption("CLV vs Random Strategy Comparison")

# Budget control
budget = st.slider("Marketing Budget (₹)", 0, 50000, 10000, step=1000)

# Load data
df = load_fake_data()

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

# Compute profits
clv_profit = df[df["customer_id"].isin(clv_selected)]["CLV"].sum()
random_profit = df[df["customer_id"].isin(random_selected)]["CLV"].sum()

# Improvement
if random_profit > 0:
    improvement_pct = ((clv_profit - random_profit) / random_profit) * 100
else:
    improvement_pct = 0

# Display tables
st.subheader("Customer Table")
st.dataframe(df, use_container_width=True)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("CLV Strategy Profit (₹)", int(clv_profit))
col2.metric("Random Strategy Profit (₹)", int(random_profit))
col3.metric("Improvement (%)", f"{improvement_pct:.2f}%")

# Insight
if clv_profit > random_profit:
    st.success("CLV-based strategy outperforms random targeting.")
else:
    st.warning("Random strategy performed better in this run.")

st.info(
    "This comparison demonstrates the economic value of using CLV-based decision making "
    "instead of naive random customer targeting."
)
