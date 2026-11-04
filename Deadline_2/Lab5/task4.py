text = input("Введите текст: ")
words = text.lower().replace('.','').replace(',','').split()
set(words)

print(f"Уникальные слова: {len(words)}")
long_words = set()

for word in words:
    if len(word) > 5:
        long_words.add(word)        
print(f"Длинные слова: {long_words}")

similarities = "python" or "programming" in words
print(f"Найдены ключевые слова: {similarities}")