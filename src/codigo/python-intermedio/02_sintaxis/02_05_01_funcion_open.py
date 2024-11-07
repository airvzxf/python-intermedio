# https://python-intermedio.readthedocs.io/es/latest/open_function.html

if __name__ == '__main__':
    print('=== Open file with bad practices ===')
    file_name = 'test-02.txt'
    f = open(file_name, 'r+')
    test_02_data = f.read()
    f.close()
    print(f'File content: {test_02_data}')

    print()
    print('=== Open file with best practices ===')
    with open(file_name, 'r+') as f:
        test_02_data = f.read()
        print(f'File content: {test_02_data}')
