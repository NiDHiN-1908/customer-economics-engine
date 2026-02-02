def decide_action(clv, threshold=5000):
    """
    Simple decision rule:
    If CLV > threshold → invest
    Else → ignore
    """
    if clv > threshold:
        return "INVEST"
    else:
        return "IGNORE"
