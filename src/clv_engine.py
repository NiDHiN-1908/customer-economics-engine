def compute_clv(monthly_revenue, churn_prob, months=12, discount_rate=0.10):
    """
    Discounted CLV formula.

    CLV = sum over t:
    (revenue * survival) / (1 + discount_rate)^t
    """

    survival = 1 - churn_prob
    clv = 0

    monthly_discount = discount_rate / 12

    for t in range(1, months + 1):
        discounted_value = (
            monthly_revenue * survival
        ) / ((1 + monthly_discount) ** t)

        clv += discounted_value

    return clv
