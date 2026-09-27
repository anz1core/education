import random
import string

def generate_random_string(length: int) -> str:
# Определяем набор символов, из которых будет состоять строка
    characters = string.ascii_letters + string.digits + string.punctuation + ' '

# Генерируем строку
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

letter = input("Введите текст для шифровки: ")
chars = 5

code_parts = []

for i in letter:
    code_parts.append(i)
    code_parts.append(generate_random_string(chars))
encoded_message = ''.join(code_parts)
print(f"Зашифрованное сообщение: {encoded_message}")