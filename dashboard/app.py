from src.cost import get_retention_cost
from src.decision_engine import optimize_budget

cost_per_customer = get_retention_cost()
selected_customers = optimize_budget(df, budget, cost_per_customer)

df["Action"] = df["customer_id"].apply(
    lambda x: "INVEST" if x in selected_customers else "IGNORE"
)
