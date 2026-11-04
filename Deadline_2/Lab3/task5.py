lines = []

while True:
    line = input("Введите строку: ")
    if line.strip() == "":
        break
    lines.append(line)

text = " ".join(lines).lower()
clean = ""

for ch in text:
    if ch.isalpha():
        clean += ch
    else:
        clean += " "

words = clean.split()
stats = {}

for word in words:
    stats[word] = stats.get(word, 0) + 1

print(f"Статистика слов: {stats}")