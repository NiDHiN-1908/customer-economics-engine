import random

def optimize_budget_clv(df, budget, cost_per_customer):
    df = df.copy()
    df["net_value"] = df["CLV"] - cost_per_customer
    df = df.sort_values("net_value", ascending=False)

    selected = []
    spent = 0

    for _, row in df.iterrows():
        if spent + cost_per_customer <= budget and row["net_value"] > 0:
            selected.append(row["customer_id"])
            spent += cost_per_customer

    return selected

def optimize_budget_random(df, budget, cost_per_customer):
    ids = list(df["customer_id"])
    random.shuffle(ids)

    selected = []
    spent = 0

    for cid in ids:
        if spent + cost_per_customer <= budget:
            selected.append(cid)
            spent += cost_per_customer

    return selected
