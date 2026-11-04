def sum_numbers(*args: float) -> float:
    return sum(args)

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

print(sum_numbers(num1, num2, num3))