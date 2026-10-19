import random


def generate_secret():
    """Генерирует 4-значное число с уникальными цифрами (первая не 0)."""
    digits = list("0123456789")
    random.shuffle(digits)
    # Первая цифра не должна быть 0
    if digits[0] == '0':
        # Меняем с первой ненулевой
        for i in range(1, len(digits)):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
    return ''.join(digits[:4])


def count_bulls_cows(secret, guess):
    """Считает быков (на месте) и коров (есть, но не на месте)."""
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


def is_valid_guess(guess):
    """Проверяет корректность ввода."""
    if len(guess) != 4:
        return False, "Нужно ввести ровно 4 цифры."
    if not guess.isdigit():
        return False, "Вводите только цифры."
    if len(set(guess)) != 4:
        return False, "Цифры не должны повторяться."
    return True, ""


def play():
    print("=" * 45)
    print("Игра «Быки и коровы»")
    print("=" * 45)
    print("Я загадал 4-значное число с уникальными цифрами.")
    print("Бык — цифра на своём месте.")
    print("Корова — цифра есть, но не на своём месте.")
    print("Введите 'выход' для завершения игры.\n")

    secret = generate_secret()
    attempts = 0

    while True:
        guess = input("Ваш вариант: ").strip()

        if guess.lower() in ("выход", "exit", "q"):
            print(f"Вы сдались. Загаданное число: {secret}")
            break

        ok, error = is_valid_guess(guess)
        if not ok:
            print(f"⚠️  {error}")
            continue

        attempts += 1
        bulls, cows = count_bulls_cows(secret, guess)

        if bulls == 4:
            print(f"\n🎉 Поздравляю! Вы угадали число {secret} за {attempts} попыток!")
            break

        print(f"  Быков: {bulls}, Коров: {cows}")

    print("\nСпасибо за игру!")


if __name__ == "__main__":
    play()
