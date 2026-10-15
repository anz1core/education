height = int(input("Введите высоту пирамиды: "))

for i in range(1, height + 1):
    print(" " * (height - 1), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(i - 1, 0, -1):
        print(k, end="")
    print()
    height -= 1