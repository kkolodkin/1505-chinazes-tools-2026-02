import random
import string


def get_yes_no(prompt: str) -> bool:
    """Запрашивает у пользователя ответ да/нет."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("да", "д", "yes", "y", "1"):
            return True
        if answer in ("нет", "н", "no", "n", "0"):
            return False
        print("Пожалуйста, введите 'да' или 'нет'.")


def get_length() -> int:
    """Запрашивает длину пароля от 1 до 100."""
    while True:
        raw = input("Введите длину пароля (от 1 до 100): ").strip()
        if not raw.isdigit():
            print("Ошибка: нужно ввести целое число.")
            continue
        length = int(raw)
        if 1 <= length <= 100:
            return length
        print("Ошибка: длина должна быть от 1 до 100.")


def generate_password(length: int, use_digits: bool,
                      use_special: bool, use_uppercase: bool) -> str:
    """Генерирует пароль по заданным условиям."""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+{}:\"<>?,./;'[]\\|/`~"

    # Обязательные наборы символов
    required_sets = [lowercase]
    if use_digits:
        required_sets.append(digits)
    if use_special:
        required_sets.append(special)
    if use_uppercase:
        required_sets.append(uppercase)

    # Общий пул символов
    pool = "".join(required_sets)

    # Если длина меньше числа обязательных наборов — предупредим
    if length < len(required_sets):
        print(f"Внимание: для всех выбранных условий нужно минимум "
              f"{len(required_sets)} символов. Будут использованы "
              f"доступные наборы без гарантии включения каждого.")

    password_chars = []

    # Гарантируем хотя бы один символ из каждого выбранного набора
    # (насколько позволяет длина)
    for char_set in required_sets:
        if len(password_chars) < length:
            password_chars.append(random.choice(char_set))

    # Добираем оставшиеся символы из общего пула
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    # Перемешиваем, чтобы обязательные символы не стояли в начале
    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=== Генератор паролей ===")

    length = get_length()
    use_digits = get_yes_no("Использовать цифры? (да/нет): ")
    use_special = get_yes_no("Использовать спецсимволы? (да/нет): ")
    use_uppercase = get_yes_no("Использовать заглавные буквы? (да/нет): ")

    # Если пользователь ничего не выбрал, кроме строчных букв — это ок,
    # но предупредим, если вообще все опции выключены и длина большая.
    if not (use_digits or use_special or use_uppercase):
        print("Примечание: используются только строчные латинские буквы.")

    password = generate_password(length, use_digits, use_special, use_uppercase)

    print("\nСгенерированный пароль:")
    print(password)


if __name__ == "__main__":
    main()
