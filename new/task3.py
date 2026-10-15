text = input("Введите текст: ")
numof_letters = 0
nums = 0
spaces = 0
numof_punct_marks = 0
num = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюQWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёЁ"
punct_marks = ".,;:!?()№%"

for i in text:
    if i in letters:
        numof_letters += 1
    if i in punct_marks:
        numof_punct_marks += 1
    if i in num:
        nums += 1
    if i ==" ":
        spaces += 1

print(f"Кол-во букв = {numof_letters}, \nКол-во цифр = {nums}, \nКол-во знаков препинания = {numof_punct_marks}, \nКол-во пробелов = {spaces} ")