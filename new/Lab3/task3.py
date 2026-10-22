phone_book = {'Захаров Денис Дмитриевич':'79822280667',
              'Петрошенко Михаил Евгенеивич':'89222789842',
              'Смирнов Алексей Дмитриевич':'79852446767'}

while True:
    action = int(input("Выберете действие: \n1 - показать все контакты\n2 - добавить контакт\n3 - удалить контакт\n4 - выйти\n"))
    if action == 1:
        for keys, values in phone_book.items():
            print(f"ФИО: {keys}, Номер телефона: {values}")
        print()
    elif action == 2:
        new_name = input("Введите ФИО нового контакта: ")
        clear_name = new_name.lower()
        if clear_name.title() in phone_book.keys():
            print(f"Имя {new_name} уже есть в контактах")
            print()
        else: 
            new_number = input("Введите номер этого контакта: ")
            phone_book[clear_name.title()] = new_number
            print()
    elif action == 3:
        del_name = input("Введите ФИО контакта который хотите удалить: ")
        clear_del_name = del_name.lower()
        if clear_del_name.title() not in phone_book:
            print(f"Контакт {del_name} не найден")
        else:
            phone_book.pop(clear_del_name.title())
    elif action == 4:
        exit()