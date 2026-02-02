def compute_clv(monthly_revenue, churn_prob, months=12):
    """
    Simple baseline CLV:
    CLV = revenue × survival × time horizon
    """
    survival = 1 - churn_prob
    clv = monthly_revenue * survival * months
    return clv
