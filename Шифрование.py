def caesar_cipher(message, n):
    result = ""
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_upper = russian_lower.upper()
    english_lower = "abcdefghijklmnopqrstuvwxyz"
    english_upper = english_lower.upper()
    for char in message:
        if char in russian_lower:
            index = russian_lower.index(char)
            result += russian_lower[(index + n) % len(russian_lower)]
        elif char in russian_upper:
            index = russian_upper.index(char)
            result += russian_upper[(index + n) % len(russian_upper)]
        elif char in english_lower:
            index = english_lower.index(char)
            result += english_lower[(index + n) % len(english_lower)]
        elif char in english_upper:
            index = english_upper.index(char)
            result += english_upper[(index + n) % len(english_upper)]
        else:
            result += char
    return result
message = input("Введите сообщение: ")
n = int(input("Введите число сдвига: "))
encrypted_message = caesar_cipher(message, n)
print("Зашифрованное сообщение:", encrypted_message)
