# https://python-intermedio.readthedocs.io/es/latest/context_managers.html

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type_value, value, traceback):
        self.file_obj.close()


if __name__ == '__main__':
    file_name_text = 'test-04.txt'

    print("=== Using custom context manager 1 ===")
    with File(file_name_text, 'w') as opened_file:
        opened_file.write('Hello Context Manager 1!')
