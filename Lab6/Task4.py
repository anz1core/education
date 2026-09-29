text = input("Введите текст: ")
start, end = map(int, input("Введите номер начальной буквы и конечной через пробел: ").split())
print(text[start-1:end])