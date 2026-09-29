password = input("Придумайте пароль: ")
conf = input("Подтвердите пароль: ")

if password != conf:
    print("Пароли не совпадают!")
else:
    login = input("Авторизуйтесь. Введите пароль: ")
    if login == password:
        print("Access")
    else:
        print("Denied")