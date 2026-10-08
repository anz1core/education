symbol = input("Введите символ: ")
height = int(input("Введите высоту: "))
width = int(input("Введите ширину: "))
i = 0

while i < height:
    o = 0
    while o < width:
        if i == 0 or o == 0 or i == height -1 or o == width -1:
            print (symbol, end="")
        else:
            print(" ", end="") 
        o += 1
    print()
    i += 1