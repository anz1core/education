from time import time
from functools import wraps

def timer(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        
        duration = end_time - start_time
        print(f"Время выполненной функции {func.__name__}: {duration}")
        
        return result
    return wrapper

@timer
def slow_func():
    for _ in range(1000000):
        pass
    
slow_func()