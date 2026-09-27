
try:
    a = float(input("Введите 1 число: "))
    b = float(input("Введите 2 число: "))
    print(f"Результат сложения: {a + b}")
    print(f"Результат вычитания: {a - b}")
    print(f"Результат умножения: {a * b}")
    print(f"Результат деления: {a / b}")
except ValueError:
    print("Введен неверный символ")
except ZeroDivisionError:
    print("Ошибка, делить на 0 нельзя")