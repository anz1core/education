colors = {
    "green": (0,255,0),
    "purple": (128,0,128),
    "red": (255,0,0),
    "blue": (0,0,255),
    "grey": (128,128,128)
}

color_1 = colors["blue"]
color_2 = colors["red"]

mixed = tuple((first + second) // 2 for first, second in zip(color_1,color_2))
print(f"Смесь {color_1} и {color_2} дает: {mixed}")

invert = colors["red"]
inverted = tuple(255 - num for num in invert)
print(f"Инвертированный {invert}: {inverted}")