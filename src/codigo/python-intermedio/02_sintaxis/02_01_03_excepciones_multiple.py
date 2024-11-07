# https://python-intermedio.readthedocs.io/es/latest/exceptions.html

if __name__ == '__main__':
    is_error_file = True
    file_name = 'test-01.txt'

    # Flip-flop the boolean value to show one trigger, one error, or the other: is_error_file.
    print('=== Multiple exceptions with commas ===')
    try:
        if is_error_file:
            file = open(file_name, 'rb')
        else:
            var = 5 / 0
    except (FileNotFoundError, ZeroDivisionError) as e:
        print(f'An FileNotFoundError or ZeroDivisionError occurred: {e.args[-1]}')

    print()
    print('=== Multiple exceptions with lines ===')
    try:
        if is_error_file:
            file = open(file_name, 'rb')
        else:
            var = 5 / 0
    except ZeroDivisionError as e:
        print(f'An ZeroDivisionError occurred: {e.args[-1]}')
    except FileNotFoundError as e:
        print(f'An FileNotFoundError occurred: {e.args[-1]}')
