from random import randint

random_num = randint(1, 100)
i = 0

while True:
    i = int(input("Введите число: "))
    if random_num == i:
        print("Угадал, возьми с полки пирожок")
        break
    elif random_num > i:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")