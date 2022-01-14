"""Программа загадывает число от 1 до 10.
Предлагает пользователю угадать это число, пока не угадает."""

import random
qest=random.randint(1,10)
answer=int(input("угадай число от 1 до 10"))
while qest != answer:
    answer = int(input("угадай число от 1 до 10"))
