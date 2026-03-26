def calculate_savings(salary, expenses):
    return salary - expenses


def calculate_health_score(salary, expenses):
    if salary == 0:
        return 0

    savings = salary - expenses
    savings_ratio = savings / salary

    if savings_ratio >= 0.4:
        return 95
    elif savings_ratio >= 0.3:
        return 85
    elif savings_ratio >= 0.2:
        return 70
    elif savings_ratio >= 0.1:
        return 55
    else:
        return 35


def calculate_sip(goal_amount, years):
    months = years * 12
    if months == 0:
        return 0
    return goal_amount / months