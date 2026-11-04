def power(number, rate=2):
    return number ** rate

num = float(input("Введите число: "))
r = input("Введите степень (или нажмите Ввод для возведения в квадрат): ")

if r == "":
    print(power(num))
else:
    print(power(num, int(r)))