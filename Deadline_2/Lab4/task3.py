to_do = []

while True:
    print('\n1 - Показать все задачи \n2 - Добавить задачу \n3 - Отметить задачу как выполненную(удалить) \n4 - Выйти')
    choice = int(input("Выберите действие: "))
    
    if choice == 1:
        if len(to_do) > 0:
            for number, task in enumerate(to_do):
                print(f"{number+1}, {task}")
        else: print("Список задач пуст!")
    if choice == 2:
        desc = input("Введите описание задачи: ")
        to_do.append(desc)
    if choice == 3:
        if len(to_do) > 0:
            print("Ваши задачи: ")
            
            for number, task in enumerate(to_do):
                print(f"{number+1}, {task}")
                
            n = int(input("\nКакую задачу выполнили? "))
            if 0 <= n-1 < len(to_do):
                remove = to_do.pop(n-1)
                print(f"Задача \"{remove}\" удалена!")
            else: print("Неверный номер!")
        else: print("Список задач пуст!")
    if choice == 4:
        exit()