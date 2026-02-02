import math

def survival_curve(churn_prob, months=12):
    """
    Generate survival probability over time using exponential decay.

    survival_t = exp(-lambda * t)
    where lambda is derived from churn probability.
    """

    # Convert churn probability to decay rate
    if churn_prob <= 0:
        churn_prob = 0.0001
    if churn_prob >= 1:
        churn_prob = 0.9999

    lam = -math.log(1 - churn_prob)

    survival_probs = []
    for t in range(1, months + 1):
        survival_t = math.exp(-lam * t)
        survival_probs.append(survival_t)

    return survival_probs
