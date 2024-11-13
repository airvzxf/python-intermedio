# https://python-intermedio.readthedocs.io/es/latest/decorators.html

from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(f'Logging: {func.__name__} was called')
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Sum function"""
    return x + x


if __name__ == '__main__':
    print('=== Example 2 ===')
    result = addition_func(4)
    print(f'Result: {result}')
