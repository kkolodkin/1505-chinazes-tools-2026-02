import requests


def run():
    url = "https://v2.jokeapi.dev/joke/Programming"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("error"):
            print("Не удалось получить шутку.")
            return

        if data.get("type") == "single":
            print(data["joke"])
        elif data.get("type") == "twopart":
            print(data["setup"])
            print(data["delivery"])
        else:
            print("Не удалось распознать формат шутки.")

    except requests.RequestException as error:
        print(f"Ошибка при запросе к API: {error}")
    except (ValueError, KeyError) as error:
        print(f"Ошибка при обработке ответа: {error}")
