import random

zagadane_chyslo = random.randint(1, 10)

print("Я загадав число від 1 до 10. Спробуй вгадати!")
sprob = 3

while sprob > 0:
    try:
        vvid = int(input("Введи своє число: "))
    except ValueError:
        print("Будь ласка, введи число!")
        continue

    if vvid == zagadane_chyslo:
        print("Вітаю! Ти вгадав число!")
        break
    elif vvid > zagadane_chyslo:
        print("Менше")
    else:
        print("Більше")
    sprob -= 1
    if sprob > 0:
        print(f"У тебе залишилось спроб: {sprob}")
    else:
        print(f"На жаль, ти не вгадав. Я загадав число {zagadane_chyslo}.")
