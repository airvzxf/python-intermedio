# https://python-intermedio.readthedocs.io/es/latest/exceptions.html

if __name__ == '__main__':
    is_error_file = True
    file_name = 'test-01.txt'

    # STEP 1: Show all the errors, first time executes the file error, then the division.
    # Flip-flop the boolean value to show one trigger, one error, or the other: is_force_error.
    print('=== Errors ===')
    if is_error_file:
        file = open(file_name, 'rb')
    else:
        var = 5 / 0

    print()
    print('Goodbye!')
