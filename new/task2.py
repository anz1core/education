num = int(input("Введите число: "))
res = 0

for i in range(1, 11):
    res = num * i
    print(f"{num} * {i} = {res}")