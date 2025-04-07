print("=== Конвертер валют ===")

from_currency = input("Из какой валюты? (например, USD): ").upper()
to_currency = input("В какую валюту? (например, EUR): ").upper()
amount = float(input("Сколько перевести?: "))

print(f"Вы хотите перевести {amount} {from_currency} в {to_currency}")