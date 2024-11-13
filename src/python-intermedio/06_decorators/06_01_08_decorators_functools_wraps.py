# https://python-intermedio.readthedocs.io/es/latest/decorators.html

from functools import wraps


def new_decorator(a_func):
    @wraps(a_func)
    def wraps_the_function():
        print("Doing something before calling a_func()")
        a_func()
        print("Doing something after calling a_func()")

    return wraps_the_function


@new_decorator
def function_to_decorate():
    print("I am the function that needs to be decorated")


if __name__ == '__main__':
    print('=== functools import wraps ===')
    print(f'function_to_decorate.__name__: {function_to_decorate.__name__}')
