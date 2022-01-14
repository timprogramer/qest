"""
Усложнение.
Число теперь от 1 до 100.
Программа говорит подсказки.
"""

import random
qest=random.randint(1,10)
answer=int(input("угадай число от 1 до 10"))
while qest != answer:
    answer = int(input("угадай число от 1 до 10"))
print("поздровляю ты выйграл 1 копейку")