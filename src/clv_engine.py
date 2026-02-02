def compute_clv(monthly_revenue, churn_prob, discount_rate=0.01):
    """
    Proper survival-based CLV.
    No costs. No penalties. No hacks.
    Pure expected future revenue.
    """

    if churn_prob <= 0:
        expected_lifetime = 60  # cap at 5 years
    else:
        expected_lifetime = 1 / churn_prob

    clv = 0
    for t in range(1, int(expected_lifetime) + 1):
        clv += monthly_revenue / ((1 + discount_rate) ** t)

    return clv
