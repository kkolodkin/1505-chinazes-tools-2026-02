import random
print("Генератор случайных чисел")
while True:
    try:
        count = int(input("Введите количество чисел (от 1 до 1000): "))
        if 1 <= count <= 1000:
            break
        else:
            print("Ошибка! Введите число от 1 до 1000.")
    except ValueError:
        print("Ошибка! Необходимо ввести целое число.")
LIMIT = 10**10
while True:
    try:
        minimum = int(input("Введите минимальное число: "))
        maximum = int(input("Введите максимальное число: "))
        if not (-LIMIT <= minimum <= LIMIT):
            print("Минимум должен быть от -10^10 до 10^10.")
            continue
        if not (-LIMIT <= maximum <= LIMIT):
            print("Максимум должен быть от -10^10 до 10^10.")
            continue
        if minimum > maximum:
            print("Ошибка! Минимум не может быть больше максимума.")
            continue
        break
    except ValueError:
        print("Ошибка! Необходимо ввести целые числа.")
numbers = [
    random.randint(minimum, maximum)
    for _ in range(count)
]
print("\n=== Результат ===")
for number in numbers:
    print(number)
print("Всего сгенерировано чисел:", len(numbers))
