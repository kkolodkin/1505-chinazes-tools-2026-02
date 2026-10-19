import random


def get_int(prompt):
    """Запрашивает у пользователя целое число с проверкой."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введите целое число.")


def get_range():
    """Запрашивает диапазон и валидирует его согласно условиям."""
    LIMIT = 10 ** 10
    while True:
        a = get_int("Введите нижнюю границу диапазона: ")
        b = get_int("Введите верхнюю границу диапазона: ")

        if not (-LIMIT <= a <= LIMIT) or not (-LIMIT <= b <= LIMIT):
            print(f"Ошибка: числа должны быть в диапазоне от -{LIMIT} до {LIMIT}.")
            continue

        if a >= b:
            print("Ошибка: нижняя граница должна быть меньше верхней.")
            continue

        return a, b


def play_game():
    """Одна партия игры."""
    print("\n=== Новая игра ===")
    a, b = get_range()
    secret = random.randint(a, b)

    print(f"Я загадал число в диапазоне от {a} до {b}. Попробуйте угадать!")

    attempts = 0
    while True:
        guess = get_int("Ваш вариант: ")
        attempts += 1

        if guess < secret:
            print("Мое число больше")
        elif guess > secret:
            print("Мое число меньше")
        else:
            print(f"\nПоздравляю! Вы угадали число {secret}!")
            print(f"Потрачено попыток: {attempts}")
            return


def main():
    print("Игра «Угадай число»")
    while True:
        play_game()
        while True:
            answer = input("\nСыграть ещё раз? (да/нет): ").strip().lower()
            if answer in ("да", "д", "yes", "y"):
                break
            if answer in ("нет", "н", "no", "n"):
                print("Спасибо за игру! До свидания.")
                return
            print("Пожалуйста, ответьте «да» или «нет».")


if __name__ == "__main__":
    main()
