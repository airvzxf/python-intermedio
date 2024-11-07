# https://python-intermedio.readthedocs.io/es/latest/exceptions.html

if __name__ == '__main__':
    file_name = 'test-01.txt'

    print()
    print('=== Try/Else ===')
    try:
        pass
    except Exception:
        print('Exception!')
    else:
        print('This is executed if no exception occurs.')
    finally:
        print("You always enter here, whether there is an exception or not.")

    print()
    print('=== Try/Else with error ===')
    try:
        file = open(file_name, 'rb')
    except Exception:
        print('Exception!')
    else:
        print('This is executed if no exception occurs.')
    finally:
        print("You always enter here, whether there is an exception or not.")
