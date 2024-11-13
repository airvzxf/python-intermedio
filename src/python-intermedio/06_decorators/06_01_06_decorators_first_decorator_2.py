# https://python-intermedio.readthedocs.io/es/latest/decorators.html

def new_decorator(a_func):
    def wraps_the_function():
        print("Doing something before calling a_func()")
        a_func()
        print("Doing something after calling a_func()")

    return wraps_the_function


@new_decorator
def function_to_decorate():
    print("I am the function that needs to be decorated")


if __name__ == '__main__':
    print('=== Your first decorator 2 ===')
    function_to_decorate()
    # The use of the @new_decorator syntax is equivalent to the following line:
    # function_to_decorate = new_decorator(function_to_decorate)
