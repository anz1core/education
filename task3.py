from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция: {func.__name__}, с аргументами: {args}")
        print(func(*args, **kwargs))
    return wrapper

@logger
def add(a,b):
    return a + b

add(5,10)