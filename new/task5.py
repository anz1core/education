count = int(input("Сколько чисел вы хотите ввести? "))
nums = []
count_greater = 0
for i in range(count):
    numbers = float(input(f"Введите число {i+1}: "))
    nums.append(numbers)

if count > 0:
    max = max(nums)
    min = min(nums)
    average = sum(nums) / count

for i in nums:
    if i > average:
        count_greater += 1

print("Результаты:")
print(f"Максимальное: {max}")
print(f"Минимальное: {min}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {count_greater}")