a, b, c = map(int, input("Введите три целых числа через пробел: ").split())

ab = a * b
bc = b * c
ca = c * a

a4 = a ** 4
rem = b % c 
div = c // a

res1 = a4
res2 = rem
res3 = div

print(f"a * b = {ab}")
print(f"b * c = {bc}")
print(f"c * a = {ca}")

print(f"a ** 4 = {res1}")
print(f"b % c = {res2}")
print(f"c // a = {res3}")

print(f"Сумма результатов 5 пункта = {res1 + res2 + res3}")