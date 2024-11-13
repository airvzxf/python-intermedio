# https://python-intermedio.readthedocs.io/es/latest/decorators.html

def hi():
    return "Hi!"


def do_this_before_hi(func):
    print("Do something before calling function")
    print(func())
    print("Do something after calling function")


if __name__ == '__main__':
    print('=== Using functions as arguments to others ===')
    do_this_before_hi(hi)
