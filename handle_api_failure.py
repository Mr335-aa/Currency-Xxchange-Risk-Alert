import requests


def get_exchange_rate(base, target):
    response = requests.get(
        "https://api.frankfurter.app/latest",
        params={"from": base, "to": target},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["rates"][target]


base = "USD"
target = "EUR"

try:
    rate = get_exchange_rate(base, target)

except requests.exceptions.RequestException:
    print("Unable to fetch exchange-rate data.")