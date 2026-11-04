def build_user_profile(user_id: int, **kwargs) -> dict:
    profile = {'user_id': user_id}
    profile.update(kwargs)
    return profile

uid = int(input("Введите ID пользователя: "))
name = input("Введите имя: ")
status = input("Введите статус: ")
email = input("Введите email: ")

profile = build_user_profile(uid, name=name, status=status, email=email)
print(profile)