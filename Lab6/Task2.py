text = input("Введите текст: ")
replace = input("Введите строку и на что хотите заменить через пробел: ").split()
new_text = text.replace(replace[0], replace[1])
print(new_text)