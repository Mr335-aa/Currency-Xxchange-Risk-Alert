from currency_api import get_exchange_rate, get_historical_rate
from validator import validate_amount, validate_currency
from risk_analyzer import calculate_percentage_change, analyze_risk 
from datetime import date, timedelta


print("===================================")
print("   Currency Exchange Calculator")
print("===================================")


base_currency = input("Enter base currency (e.g. USD): ").upper()
target_currency = input("Enter target currency (e.g. INR): ").upper()
amount_input = input("Enter amount: ")

if not validate_currency(base_currency):
    print("Invalid base currency.")
    exit()

if not validate_currency(target_currency):
    print("Invalid target currency.")
    exit()

if not validate_amount(amount_input):
    print("Invalid amount. Please enter a positive number.")
    exit()

amount = float(amount_input)

try:
    current_rate = get_exchange_rate(base_currency, target_currency)

    yesterday = date.today() - timedelta(days=1)
    previous_rate = get_historical_rate(
        base_currency,
        target_currency,
        yesterday.strftime("%Y-%m-%d")
    )

    converted_amount = amount * current_rate

    change_percentage = calculate_percentage_change(
        current_rate,
        previous_rate
    )

    risk_level, risk_message = analyze_risk(change_percentage)

except Exception as error:
    print("\nUnable to fetch exchange-rate data.")
    print("Please check:")
    print("1. Your internet connection")
    print("2. The currency codes")
    print("3. Whether the currency is supported")
    print("\nProgram ended safely.")
    exit()

    
print("\n---------- Result ----------")
print("Base Currency:", base_currency)
print("Target Currency:", target_currency)
print("Amount:", amount)
print("Exchange Rate:", current_rate)
print("Converted Amount:", round(converted_amount, 2))
print("Previous Rate:", previous_rate)
print("Rate Change:", round(change_percentage, 2), "%")
print("Risk Level:", risk_level)
print("Alert:", risk_message)