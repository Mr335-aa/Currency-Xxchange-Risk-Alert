def calculate_percentage_change(current_rate, previous_rate):
    change = ((current_rate - previous_rate) / previous_rate) * 100
    return change


def analyze_risk(change_percentage):

    absolute_change = abs(change_percentage)

    if absolute_change < 2:
        return "LOW", "Normal exchange-rate movement."

    elif absolute_change <= 5:
        return "MEDIUM", "Moderate exchange-rate movement detected."

    else:
        return "HIGH", "Significant exchange-rate movement detected."