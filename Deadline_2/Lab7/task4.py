call_counter = 0
def increment_counter() -> None:
    global call_counter
    call_counter += 1
times = int(input("Сколько раз вызвать фнкцию? "))

for i in range(times):
    increment_counter()
print(call_counter)