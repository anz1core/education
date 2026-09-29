text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

count = text.count(word)
index = text.find(word)
clean_text = text.replace(word, "")

print(f"Количество слов: {count}, Индекс первого слова: {index+1}")
print(f"Текст без слова: {clean_text}")