
a = float(input("Введи перше число (a): "))
b = float(input("Введи друге число (b): "))


operation = input("Вибери математичну операцію (+, -, *, /): ")


if operation == "+":
    result = a + b
    print(f"Результат: {a} + {b} = {result}")
elif operation == "-":
    result = a - b
    print(f"Результат: {a} - {b} = {result}")
elif operation == "*":
    result = a * b
    print(f"Результат: {a} * {b} = {result}")
elif operation == "/":
    if b == 0:
        print("Ділення на нуль неможливе!")
    else:
        result = a / b
        print(f"Результат: {a} / {b} = {result}")
else:
    print("Невідома операція! Будь ласка, вибери одну з наступних: +, -, *, /.")
