i = int(input("Введите положительное число: "))
digits = 0
temp_num = i

while temp_num > 0:
    last = temp_num % 10
    digits += last
    temp_num = temp_num // 10
print(f"Сумма цифр числа {i}: {digits}")