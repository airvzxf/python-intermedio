# https://python-intermedio.readthedocs.io/es/latest/context_managers.html

from contextlib import contextmanager


@contextmanager
def open_file(name):
    file_handler = open(name, 'w')
    try:
        yield file_handler
    finally:
        file_handler.close()


if __name__ == '__main__':
    file_name_text = 'test-04.txt'

    print("=== Using custom context manager 2 ===")
    with open_file(file_name_text) as f:
        f.write('Hello Context Manager 2!')
