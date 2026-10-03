def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_currency(currency):
    if len(currency) != 3:
        return False

    if not currency.isalpha():
        return False

    return True