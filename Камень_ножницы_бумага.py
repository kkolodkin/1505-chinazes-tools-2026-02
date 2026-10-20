import random

# Варианты выбора
choices = ["камень", "ножницы", "бумага"]

# Счёт
player_score = 0
computer_score = 0

print("Камень, ножницы, бумага")
print("Вводи: камень, ножницы или бумага. Для выхода напиши 'выход'.")

while True:
    player = input("\nТвой выбор: ").lower().strip()

    if player == "выход":
        break

    if player not in choices:
        print("Неверный ввод, попробуй снова.")
        continue

    computer = random.choice(choices)
    print("Компьютер выбрал:", computer)

    # Определяем победителя
    if player == computer:
        print("Ничья")
    elif (player == "камень" and computer == "ножницы") or \
         (player == "ножницы" and computer == "бумага") or \
         (player == "бумага" and computer == "камень"):
        print("Ты выиграл")
        player_score += 1
    else:
        print("Ты проиграл")
        computer_score += 1

    print("Счёт: ты", player_score, "-", computer_score, "компьютер")

# Итог
print("\nИгра окончена")
print("Ты:", player_score, "| Компьютер:", computer_score)

if player_score > computer_score:
    print("Ты победил в игре")
elif player_score < computer_score:
    print("Компьютер победил в игре")
else:
    print("Ничья в игре")
