import math

users_input = input("Введите выражение (например, 6 - 7): ").split()
operator = users_input[1]

if operator != '/**':
    
    num_1 = float(users_input[0])
    num_2 = float(users_input[2])
    
    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == '/':
        print(num_1 / num_2)
    elif operator == '%':
        print(num_1 % num_2)
    elif operator == '//':
        print(num_1 // num_2)
    elif operator == '**':
        print(num_1 ** num_2)
    elif operator == '%%':
        print(num_2 / 100 * num_1)
    else:
        print("Неизвестный оператор")
else:
    num_1 = float(users_input[0])
    print(math.sqrt(num_1))