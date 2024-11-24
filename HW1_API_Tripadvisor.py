import os
import requests
from dotenv import load_dotenv
import json
import sys

sys.stdin.reconfigure(encoding='utf-8')

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "https://api.content.tripadvisor.com/api/v1/location/search"
city = input("Введите название города: ").strip()
params = {
    "key": os.getenv("API_KEY"),
    "searchQuery": city,
    "language": "ru",
    "limit": 5
}

headers = {"accept": "application/json"}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос API!")
    data = response.json()
    venues = data.get("data", [])

    if venues:
        print("\nРезультаты поиска:")
        for venue in venues:
            name = venue.get("name", "Не указано")
            address_obj = venue.get("address_obj", {})
            city = address_obj.get("city", "Город не указан")

            # Печатаем результат в удобном формате
            print(f"Место: {name}")
            print(f"Город: {city}")
            print(f"Адрес: {address_obj.get('address_string', 'Адрес не указан')}")
            print("-" * 50)
    else:
        print("Никаких результатов не найдено.")
else:
    print(f"Ошибка {response.status_code}: {response.text}")
