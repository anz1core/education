from random import randint

l = [randint(1,100) for i in range(10)]
even = []
more_fifty = []

for i in l:
    if i % 2 == 0:
        even.append(i)
    if i > 50:
        more_fifty.append(i)

print(f"Стартовый список: {l}")
print(f"Четные числа: {even}")
print(f"Числа больше 50: {more_fifty}")