from src.survival import survival_curve

def compute_clv(monthly_revenue, churn_prob, months=12, discount_rate=0.10):
    """
    Full economic CLV with survival + discounting.

    CLV = sum_t ( revenue * survival_t * discount_t )

    survival_t comes from survival curve.
    discount_t = 1 / (1 + r/12)^t
    """

    survival_probs = survival_curve(churn_prob, months)
    monthly_discount = discount_rate / 12

    clv = 0

    for t in range(1, months + 1):
        survival_t = survival_probs[t - 1]
        discount_t = 1 / ((1 + monthly_discount) ** t)
        clv += monthly_revenue * survival_t * discount_t

    return clv
