text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

if word in text:
    count = text.count(word)
    print(f"Слово найдено! Количество: {count}")
else:
    print("Слово не найдено.")