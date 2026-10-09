list = []
for i in range(5):
    num = float(input(f"Введите {i+1} число: "))
    list.append(num)
    
print(f"Минимальное число: {min(list)}")
print(f"Максимальное число: {max(list)}")