# https://python-intermedio.readthedocs.io/es/latest/exceptions.html

if __name__ == '__main__':
    file_name = 'test.txt'

    # Flip-flop the boolean value to show one trigger, one error, or the other: is_error_file.
    print('=== Finally ===')
    try:
        file = open(file_name, 'rb')
    except FileNotFoundError as e:
        print(f'An FileNotFoundError occurred: {e.args[-1]}')
    finally:
        print("You always enter here, whether there is an exception or not.")

    print()
    print('=== Finally ===')
    try:
        pass
    except FileNotFoundError as e:
        print(f'An FileNotFoundError occurred: {e.args[-1]}')
    finally:
        print("You always enter here, whether there is an exception or not.")
