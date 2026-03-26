def tax_suggestion(salary):
    if salary <= 500000:
        return "No tax or very low tax. Focus on saving."
    elif salary <= 1000000:
        return "Invest in 80C (PPF, ELSS, LIC) to save tax."
    else:
        return "Use 80C + 80D + NPS for maximum tax saving."