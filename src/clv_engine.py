from src.survival import survival_curve
from src.cost import get_retention_cost

def compute_clv(monthly_revenue, churn_prob, months=12, discount_rate=0.10):
    """
    Profit-aware discounted CLV with survival.

    CLV = sum_t ( (revenue - retention_cost) 
                  * survival_t 
                  * discount_t )
    """

    survival_probs = survival_curve(churn_prob, months)
    monthly_discount = discount_rate / 12
    retention_cost = get_retention_cost()

    clv = 0

    for t in range(1, months + 1):
        survival_t = survival_probs[t - 1]
        discount_t = 1 / ((1 + monthly_discount) ** t)
        monthly_profit = monthly_revenue - retention_cost
        clv += monthly_profit * survival_t * discount_t

    return clv
