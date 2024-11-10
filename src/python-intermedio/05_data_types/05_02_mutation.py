# https://python-intermedio.readthedocs.io/es/latest/mutation.html

def append_number(num, target=[]):
    target.append(num)
    return target


def append_number_fixed(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target


if __name__ == '__main__':
    print("=== Mutation ===")

    print()
    print('=== Assign a variable to another mutable variable ===')
    foo = ['hola']
    print(f'foo: {foo}')

    bar = foo
    bar += ['adios']
    print(f'foo: {foo}')
    print(f'bar: {bar}')

    print()
    print('=== Default arguments in a function ===')
    print(f'append_number(1): {append_number(1)}')
    print(f'append_number(2): {append_number(2)}')
    print(f'append_number(3): {append_number(3)}')

    print()
    print('=== Fixed: default arguments in a function ===')
    print(f'append_number_fixed(1): {append_number_fixed(1)}')
    print(f'append_number_fixed(2): {append_number_fixed(2)}')
    print(f'append_number_fixed(3): {append_number_fixed(3)}')
