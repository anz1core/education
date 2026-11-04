def find_max(a, b):
    if a > b:
        return a
    else:
        return b
    
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
max_num = find_max(num1, num2)
print(f"Большее число: {max_num}")