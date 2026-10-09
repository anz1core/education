text = input("Введите строку: ")
clear_text = text.lower().replace(" ", "")
left = 0
right = len(clear_text) - 1
palindrom = True

while left < right:
    if clear_text[left] != clear_text[right]:
        palindrom = False
        break
    left += 1
    right -= 1
if palindrom:
    print("Это палиндром")
else:
    print("Это не палиндром")