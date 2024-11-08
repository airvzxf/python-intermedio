# https://python-intermedio.readthedocs.io/es/latest/context_managers.html

if __name__ == '__main__':
    file_name = 'test-04.txt'

    print("=== Using context manager ===")
    with open(file_name, 'w') as opened_file:
        opened_file.write('Hello world!')

    print()
    print("=== Using exceptions ===")
    file = open(file_name, 'w')
    try:
        file.write('Hello universe!')
    finally:
        file.close()
