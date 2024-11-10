# https://python-intermedio.readthedocs.io/es/latest/classes.html

class OldClass():
    def __init__(self):
        print('I am an old class')


class NewClass(object):
    def __init__(self):
        print('I am a jazzy new class')


if __name__ == '__main__':
    print("=== New style of classes ===")
    old = OldClass()
    new = NewClass()
