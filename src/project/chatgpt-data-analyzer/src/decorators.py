from time import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'{func.__name__} ejecutado en {end_time - start_time:.4f} segundos')
        return result

    return wrapper
