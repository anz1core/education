text = input("Введите строку: ")
letters = "еёаиоуыэюяaeiouyАЕЁОУЫЭЮЯAEIOUY"
res = ""
a = 0

while a < len(text):
    if text[a] not in letters:
        res += text[a]
    a+=1
    
print(f"Результат: {res}")