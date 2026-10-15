word = input("Введите текст: ")
clear_word = word.lower()
list = {}

for i in clear_word:
    if i in list.keys():
        list[i] += 1
    else: 
        list[i] = 1
print(list)