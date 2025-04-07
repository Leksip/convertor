import requests
from config import API_URL, API_KEY


def get_conversion_rate(from_currency: str, to_currency: str) -> float:
    """Получаем курс валют с API"""
    url = f"{API_URL}/{API_KEY}/pair/{from_currency}/{to_currency}"
    print(url)
    response = requests.get(url)
    data = response.json()

    try:
          if data.get('result') == 'success':
              return data["conversion_rate"]
          else:
             error_info = data.get('error', {}).get('info', 'Неизвестная ошибка')
             raise ValueError(error_info)

    except requests.exceptions.RequestException as error:
        print(f'Request Exception: {error}')