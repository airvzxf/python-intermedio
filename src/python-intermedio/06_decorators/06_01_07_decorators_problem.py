# https://python-intermedio.readthedocs.io/es/latest/decorators.html

def new_decorator(a_func):
    def wraps_the_function():
        print("Doing something before calling a_func()")
        a_func()
        print("Doing something after calling a_func()")

    return wraps_the_function


def function_to_decorate():
    print("I am the function that needs to be decorated")


if __name__ == '__main__':
    print('=== Problem ===')
    function_to_decorate()

    print()
    print('=== Creating a decorator ===')
    function_to_decorate = new_decorator(function_to_decorate)

    print()
    print('=== Using a decorator ===')
    function_to_decorate()

    print()
    print('=== Function __name__ ===')
    print(f'function_to_decorate.__name__: {function_to_decorate.__name__}')
