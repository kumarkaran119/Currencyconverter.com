def currency_converter(amount, from_currency, to_currency):
    rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.75, 'INR': 73.21},
        'EUR': {'USD': 1.18, 'GBP': 0.88, 'INR': 88.68},
        'GBP': {'USD': 1.33, 'EUR': 1.14, 'INR': 100.25},
        'INR': {'USD': 0.014, 'EUR': 0.011, 'GBP': 0.01}
    }

    if from_currency == to_currency:
        return amount

    if from_currency in rates and to_currency in rates[from_currency]:
        converted_amount = amount * rates[from_currency][to_currency]
        return converted_amount
    else:
        return "Conversion rate not available."

amount_to_convert = int(input("Enter an ammount to Convert :-"))
converted_amount = currency_converter(amount_to_convert, 'USD', 'EUR')
print(f"${amount_to_convert} USD is approximately {converted_amount} EUR.")