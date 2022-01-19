"""
Добавляем счетчик попыток.
"""

import random

qest=random.randint(1,100)
answer=int(input("угадай число от 1 до 100"))
p=1
while qest != answer:
    if answer<qest:
        print("число больше")


    elif answer > qest:
        print("число меньше")
    answer = int(input("угадай число от 1 до 100"))
    p=p+1
print("поздровляю ты выйграл 1 копейку")
print("ты угадал за",p,"попыток")