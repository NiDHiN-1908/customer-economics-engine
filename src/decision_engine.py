import random

def optimize_budget_clv(df, budget, cost_per_customer):
    """
    Strategy 1: CLV-based optimization.
    Select highest CLV customers under budget.
    """
    df_sorted = df.sort_values("CLV", ascending=False)

    selected = []
    spent = 0

    for _, row in df_sorted.iterrows():
        if spent + cost_per_customer <= budget:
            selected.append(row["customer_id"])
            spent += cost_per_customer

    return selected


def optimize_budget_random(df, budget, cost_per_customer):
    """
    Strategy 2: Random targeting.
    Select random customers under budget.
    """
    customers = df["customer_id"].tolist()
    random.shuffle(customers)

    selected = []
    spent = 0

    for cust_id in customers:
        if spent + cost_per_customer <= budget:
            selected.append(cust_id)
            spent += cost_per_customer

    return selected
