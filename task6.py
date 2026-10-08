symbol = input("Введите символ: ")
height = int(input("Введите высоту: "))
width = int(input("Введите ширину: "))
i = 0

while i < height:
    o = 0
    while o < width:
        print(symbol, end="")
        o += 1
    print()
    i += 1