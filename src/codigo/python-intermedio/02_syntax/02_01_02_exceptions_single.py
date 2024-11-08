# https://python-intermedio.readthedocs.io/es/latest/exceptions.html

if __name__ == '__main__':
    file_name = 'test-01.txt'

    print('=== Single exception ===')
    try:
        file = open(file_name, 'rb')
    except FileNotFoundError as e:
        print(f'An FileNotFoundError occurred: {e.args[-1]}')

    print()
    print('=== Single exception ===')
    try:
        pass
    except FileNotFoundError as e:
        print(f'An FileNotFoundError occurred: {e.args[-1]}')

    # Explain that it shows the "goodbye" message.
    print()
    print('Goodbye!')
