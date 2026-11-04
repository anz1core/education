print("Введите текст: ")

lines = []
while True:
    line = input()
    if line == '':
        break
    lines.append(line)
text = " ".join(lines)

for ch in text:
    if not ch.isalpha():
        text = text.replace(ch, " ")
words = text.lower().split()

if not words:
    print("Слов нет")
else:
    longest = words[0]
    shortest = words[0]
    total = 0
    for i in words:
        total += len(i)
        if len(i) > len(longest):
            longest = i
        if len(i) < len(shortest):
            shortest = i
            
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
        
    top = sorted(freq.items(), key=lambda x: -x[1])[:5]
    
    print(f"Самое длинное слово: {longest}")
    print(f"Самое короткое слово: {shortest}")
    print(f"Средняя длинна: {round(total / len(words),1)}")
    print(f"Топ-5 слов: {top}")