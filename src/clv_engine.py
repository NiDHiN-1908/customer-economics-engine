def compute_clv(monthly_revenue, churn_prob, months=12):
    """
    Baseline CLV formula (v1):
    CLV = revenue × survival × time horizon
    """
    survival = 1 - churn_prob
    clv = monthly_revenue * survival * months
    return clv
