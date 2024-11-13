# https://python-intermedio.readthedocs.io/es/latest/decorators.html

def hello(nombre="Stephanie"):
    return "Hola " + nombre


if __name__ == '__main__':
    print('=== Everything is an object in Python ===')
    print(f'hello(): {hello()}')

    # We can assign a function to a variable
    greetings = hello
    # We don't use () because we are not calling it, but rather
    # we are assigning it to a variable.

    print(f'greetings(): {greetings()}')

    # We can also remove the function assigned to the variable with `del`.
    del hello
    # This will raise an error because the function `hello` no longer exists.
    print(f'hello(): {hello()}')

    print(f'greetings(): {greetings()}')
