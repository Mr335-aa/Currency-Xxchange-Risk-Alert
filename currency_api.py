import requests


def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.frankfurter.dev/v2/rate/{base_currency}/{target_currency}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    return data["rate"]


def get_historical_rate(base_currency, target_currency, date):
    url = f"https://api.frankfurter.dev/v2/rate/{base_currency}/{target_currency}?date={date}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    return data["rate"]


