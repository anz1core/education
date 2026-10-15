num = int(input("Введите число: "))
res = 0

for i in range(1, num + 1):
    res += i

print(f"Сумма чисел от 1 до {num} = {res}")