# https://python-intermedio.readthedocs.io/es/latest/decorators.html

from functools import wraps


def logit(logfile='test-05.log'):
    def logging_decorator(func):
        @wraps(func)
        def with_logging(*args, **kwargs):
            log_string = f'Logging: {func.__name__} was called'
            print(log_string)

            # Open the file and add its content.
            with open(logfile, 'w') as opened_file:
                # We write the content in the file.
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return with_logging

    return logging_decorator


# NOTE: If the decorator is without the parentheses, the decorator will not work.
@logit()
def addition_func(x):
    """Sum function"""
    print(f'Sum function | x: {x}')
    return x + x


@logit(logfile='test-06.log')
def subtraction_func(x):
    """Subtraction function"""
    print(f'Subtraction function | x: {x}')
    return x - 1


if __name__ == '__main__':
    print('=== Nesting a Decorator inside a Function ===')
    result_addition = addition_func(4)
    print(f'Result addition: {result_addition}')

    print()
    result_subtraction = subtraction_func(5)
    print(f'Result subtraction: {result_subtraction}')
