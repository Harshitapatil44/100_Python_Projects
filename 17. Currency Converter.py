rates = {
    "INR": 1,
    "USD": 83.5,
    "EUR": 90.2,
    "GBP": 105.7,
    "JPY": 0.56
}

print("Available currencies:", rates.keys())

from_currency = input("Enter from currency: ").upper()
to_currency = input("Enter to currency: ").upper()
amount = float(input("Enter amount: "))

if from_currency in rates and to_currency in rates:
    amount_in_inr = amount * rates[from_currency]
    converted = amount_in_inr / rates[to_currency]

    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Invalid currency entered")
