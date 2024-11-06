# https://python-intermedio.readthedocs.io/es/latest/ternary_operators.html

def my_function(real_name, optional_name=None):
    display_name = optional_name or real_name
    print(display_name)


if __name__ == '__main__':
    print('=== Ternary Operators #1 ===')
    is_beautiful = True
    state = 'It is beautiful.' if is_beautiful else 'It is not beautiful.'
    print(state)

    is_beautiful = False
    state = 'It is beautiful.' if is_beautiful else 'It is not beautiful.'
    print(state)

    print()
    print('=== Ternary Operators #2 ===')
    is_beautiful = True
    appearance = ('Ugly', 'Beautiful')[is_beautiful]
    print(f'The cat is {appearance}')

    is_beautiful = False
    appearance = ('Ugly', 'Beautiful')[is_beautiful]
    print(f'The cat is {appearance}')

    print()
    print('=== Ternary Operators #3 ===')
    condition = True
    print(2 if condition else 1 / 0)
    # It will raise a ZeroDivisionError.
    # print((1/0, 2)[condition])

    print()
    print('=== Ternary Operators #4 ===')
    print(True or 'False string value')
    print(False or 'True string value')

    output = None
    message = output or "Nothing was returned."
    print(message)

    my_function("Ashley")
    my_function("Britany", "Fanny")
