# https://python-intermedio.readthedocs.io/es/latest/global_&_return.html

def sum_function(value_1, value_2):
    return value_1 + value_2


def sum_global_function(value_1, value_2):
    global result_global
    result_global = value_1 + value_2


if __name__ == '__main__':
    print('=== Return function ===')
    result = sum_function(3, 5)
    print(f'The result is: {result}')

    print()
    print('=== Global variable ===')
    sum_global_function(2, 13)
    print(f'The result is: {result_global}')
