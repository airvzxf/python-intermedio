# https://python-intermedio.readthedocs.io/es/latest/context_managers.html

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type_value, value, traceback):
        print(f'*** Error:')
        print(f'    * Type: {type_value}')
        print(f'    * Value: {value}')
        print(f'    * Traceback: {traceback}')
        self.file_obj.close()


class File2(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type_value, value, traceback):
        print("The exception was handled.")
        self.file_obj.close()
        return True


if __name__ == '__main__':
    file_name_text = 'test-04.txt'

    print("=== Context manager handling the error ===")
    with File2(file_name_text, 'w') as opened_file:
        opened_file.undefined_function('Hello Exception 1!')

    print()
    print("=== Context manager without error handling ===")
    with File(file_name_text, 'w') as opened_file:
        opened_file.undefined_function('Hello Exception 1!')
