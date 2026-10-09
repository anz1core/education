dir = input("Введите направление (left, right, straight, back): ")

if dir == "left":
    print("Иду влево")
elif dir == "right":
    print("Иду вправо")
elif dir == "straight":
    print("Иду прямо")
elif dir == "back":
    print("Иду назад")
else:
    print("Неправильное направление")