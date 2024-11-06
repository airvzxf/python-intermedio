# https://python-intermedio.readthedocs.io/es/latest/exceptions.html

if __name__ == '__main__':
    is_error_file = True
    file_name = 'test.txt'

    # Flip-flop the boolean value to show one trigger, one error, or the other: is_error_file.
    print()
    print('=== General exceptions ===')
    try:
        if is_error_file:
            file = open(file_name, 'rb')
        else:
            var = 5 / 0
    except Exception as e:
        print(f'An Exception occurred: {e.args[-1]}')
        pass
