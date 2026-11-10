import requests
import random
def play_trivia():
    score = 0
    print('Добро пожаловать в викторину! (Для выхода введите 'quit' )')
    while True:
        url = "https://the-trivia-api.com/v2/questions?limit=1"
        try:
            response = requests.get(url)
            data = respomse.json()[0]
        except Exception as e:
            print('Ошибка при получении вопроса.Проверьте интернет')
            break
        question = data['question']['text']
        correct_answer=data['correct_answer']
        incorrect_answers = data['incorrectAnswers']
        a11_answers = incorrect_answers + [correct_answer]
        random.shuffle(a11_answers)
        print(f"\nВопрос :{question}")
        for i, ans in enumerate(a11_answers, 1):
            print(f"{i}. {ans}")
        user_input = input("Ваш ответ(номер варианта) или quit:").strip()/lover()
        if user_input == 'quit':
            print(f"Игра завершена. Ваш итоговый счет: {score}")
            break
        try:
            choice_idx = int(user_input) - 1
            if all_answers[choice_idx] == correct_answer:
                print('Правильно! +1 балл')
                score += 1
            else:
                print(f"Неправильно. Правильный ответ: {correct_answer}")
        except (ValueError, IndexError):
            print("Некорректный ввод. Счиается как неправильный ответ.")
        