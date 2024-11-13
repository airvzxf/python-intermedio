# https://python-intermedio.readthedocs.io/es/latest/decorators.html

def hi(nombre='Jaime'):
    def greet():
        return 'You are inside the greet() function'

    def welcome():
        return 'You are inside the welcome() function'

    if nombre == 'Jaime':
        return greet
    else:
        return welcome


if __name__ == '__main__':
    print('=== Returning functions from functions ===')
    # That is, the variable 'a' now points to the function
    # greet() declared inside hi(). So we can call it.
    a = hi()
    print(a)
    print(a())

    b = hi('Johan')
    print(b)
    print(b())
