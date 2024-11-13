# https://python-intermedio.readthedocs.io/es/latest/decorators.html

from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated():
        print(f'can_run: {can_run}')
        if not can_run:
            return "The function will not be executed"
        return f()

    return decorated


@decorator_name
def function_to_decorate():
    return "The function is running"


if __name__ == '__main__':
    print('=== Example ===')
    can_run = True
    print(f'func(): {function_to_decorate()}')

    can_run = False
    print()
    print(f'func(): {function_to_decorate()}')
