"""
Добавляем условие досрочного выхода.
Например, при вводе слова "Сдаюсь"
"""

import random

qest = random.randint(1, 100)
answer = input("угадай число от 1 до 100")

p = 1

answer = int(answer)
while qest != answer:
    answer = str(answer)

    if answer == "дурацкий апорат хватит с меня деньги тоскать":
        print("ну ладно")
        print("число было",qest)
        exit()
    answer = int(answer)
    if answer < 1 or answer > 100:
        print("перестань и пишы нормально")
        answer = input("угадай число от 1 до 100")
        p = p + 1
        continue

    if answer < qest:
        print("число больше")

    elif answer > qest:
        print("число меньше")
    answer = int(input("угадай число от 1 до 100"))




    p = p + 1
print("поздровляю ты выйграл 1 копейку")
print("ты угадал за", p, "попыток")
