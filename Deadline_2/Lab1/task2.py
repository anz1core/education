num = 1
count = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    count += 1
    
print(f"Кол-во чисел: {count}")