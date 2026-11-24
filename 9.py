import requests

def get_country_info():
    # Запрашиваем у пользователя название страны
    country_name = input("Введите название страны на английском (например, Russia, USA, Japan): ").strip()

    if not country_name:
        print("Название страны не введено.")
        return

    # Формируем ссылку согласно заданию
    url = f"https://api.restcountries.com/countries/v5/names.common/{country_name}"

    # Токен из задания
    token = "rc_live_demo"

    # Передаем токен в заголовках запроса (стандартный способ авторизации)
    headers = {
        "Authorization": f"Bearer {token}"
    }

    print(f"\nЗапрос данных о стране: {country_name}...\n")

    try:
        # Отправляем GET-запрос
        response = requests.get(url, headers=headers)

        # Проверяем, успешен ли запрос (код 200)
        response.raise_for_status()

        # Преобразуем ответ в формат JSON
        data = response.json()

        # API обычно возвращает список стран (даже если найдена одна)
        if isinstance(data, list) and len(data) > 0:
            country = data[0]

            # Извлекаем нужные данные. Если данных нет, выводим "Нет данных"
            name = country.get('name', {}).get('common', 'Неизвестно')
            capital = country.get('capital', ['Нет данных'])[0]
            region = country.get('region', 'Неизвестно')
            population = country.get('population', 'Неизвестно')
            currencies = country.get('currencies', {})
            currency_names = ", ".join([c.get('name', '') for c in currencies.values()]) if currencies else "Нет данных"

            # Выводим результат
            print("-" * 30)
            print(f"Страна:    {name}")
            print(f"Столица:   {capital}")
            print(f"Регион:    {region}")
            print(f"Население: {population:,} чел.")
            print(f"Валюта:    {currency_names}")
            print("-" * 30)

        else:
            print("Страна не найдена или API вернуло пустой ответ.")

    except requests.exceptions.HTTPError as errh:
        print(f"Ошибка HTTP: {errh}")
        print("Возможно, страна не найдена. Проверьте правильность написания (на английском).")
    except requests.exceptions.ConnectionError:
        print("Ошибка соединения. Проверьте интернет.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск функции
if __name__ == "__main__":
    get_country_info()
