def display_user_profile(name, age, city):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")
    
name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город: ")
display_user_profile(age=age, name=name, city=city)