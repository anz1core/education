def simple_calculator(num1,num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else: 
            print("\nДелить на 0 нельзя!")
            exit()
            
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
oper = input("Введите оператор: ")
result = simple_calculator(a,b,oper)
print(f"\nРезультат: {result}")