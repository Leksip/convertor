from currency import get_conversion_rate


def convert_currency():
    print("=== Конвертер валют ===")
    from_currency = input("Из какой валюты? (например, USD): ").upper()
    to_currency = input("В какую валюту? (Например, RUB): ").upper()

    try:
        result = get_conversion_rate(from_currency, to_currency)
        print (f'1 {from_currency} = {result:.2f} {to_currency}')
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    convert_currency()
