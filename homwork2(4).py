try:
    start = int(input("Введи число З якого почати: "))
    end = int(input("Введи число ПО яке завершити: "))
    if start > end:
        print("️ Перше число має бути менше або рівне другому.")
    else:
        print(f" Числа від {start} до {end}:")
        for i in range(start, end + 1):
            print(i)
except ValueError:
    print(" Будь ласка, введи правильні числа!")
