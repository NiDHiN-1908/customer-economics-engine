def optimize_budget(df, budget, cost_per_customer):
    """
    Select customers with highest CLV under budget constraint.
    Greedy knapsack (sorted by CLV).
    """
    df_sorted = df.sort_values("CLV", ascending=False)

    selected = []
    spent = 0

    for _, row in df_sorted.iterrows():
        if spent + cost_per_customer <= budget:
            selected.append(row["customer_id"])
            spent += cost_per_customer

    return selected
