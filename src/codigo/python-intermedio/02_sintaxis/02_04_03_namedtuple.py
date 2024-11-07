# https://python-intermedio.readthedocs.io/es/latest/global_&_return.html

from collections import namedtuple


def profile():
    person = namedtuple('Person', 'name age')
    return person(name="Natasha", age=31)


if __name__ == '__main__':
    # Using the namedtuple
    print('=== Return namedtuple and used as a properties ===')
    p = profile()
    print(p, type(p))
    print(f'Name: {p.name} | Age: {p.age}')

    # Another way to use the namedtuple
    print()
    print('=== Return namedtuple and used as a tuple ===')
    p = profile()
    print(f'Name: {p[0]} | Age: {p[1]}')

    # Unpacking can also be done
    print()
    print('=== Return namedtuple and assign into the variables ===')
    nombre, edad = profile()
    print(f'Name: {nombre} | Age: {edad}')
