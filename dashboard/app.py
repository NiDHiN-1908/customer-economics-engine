import sys
import os
import numpy as np

# Make project root visible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.data_pipeline import load_fake_data
from src.clv_engine import compute_clv
from src.cost import get_retention_cost
from src.decision_engine import optimize_budget_clv, optimize_budget_random

st.set_page_config(page_title="Customer Economics Engine", layout="wide")

st.title("Customer Economics Engine")
st.caption("Risk-Aware CLV Strategy Comparison")

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

# Profit distributions (simulate uncertainty)
def simulate_profit(selected_ids, n_sim=1000):
    profits = []
    for _ in range(n_sim):
        noise = np.random.normal(1, 0.15)  # 15% volatility
        profit = df[df["customer_id"].isin(selected_ids)]["CLV"].sum()
        profits.append(profit * noise)
    return np.array(profits)

clv_dist = simulate_profit(clv_selected)
random_dist = simulate_profit(random_selected)

# Stats
clv_mean = clv_dist.mean()
clv_low = np.percentile(clv_dist, 10)
clv_high = np.percentile(clv_dist, 90)

random_mean = random_dist.mean()
random_low = np.percentile(random_dist, 10)
random_high = np.percentile(random_dist, 90)

# Improvement
improvement_pct = ((clv_mean - random_mean) / random_mean) * 100

# Display table
st.subheader("Customer Table")
st.dataframe(df, use_container_width=True)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("CLV Strategy (Expected ₹)", int(clv_mean))
col2.metric("Random Strategy (Expected ₹)", int(random_mean))
col3.metric("Improvement (%)", f"{improvement_pct:.2f}%")

# Risk view
st.subheader("Risk Analysis (10% – 90% Range)")

risk_col1, risk_col2 = st.columns(2)
risk_col1.metric("CLV Worst Case (₹)", int(clv_low))
risk_col1.metric("CLV Best Case (₹)", int(clv_high))

risk_col2.metric("Random Worst Case (₹)", int(random_low))
risk_col2.metric("Random Best Case (₹)", int(random_high))

# Insight
if clv_mean > random_mean:
    st.success("CLV-based strategy dominates even under uncertainty.")
else:
    st.warning("Random strategy performed better under uncertainty.")

st.info(
    "This version models uncertainty using Monte Carlo simulation. "
    "Decisions are evaluated using expected value and risk bounds, "
    "not single-point estimates."
)
