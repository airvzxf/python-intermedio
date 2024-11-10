# https://python-intermedio.readthedocs.io/es/latest/classes.html

class Cal(object):
    # Pi is a class variable
    pi = 3.142

    def __init__(self, radio):
        # self.radio is an instance variable
        self.radio = radio

    def area(self):
        return self.pi * (self.radio ** 2)


class SuperClass(object):
    superpowers = []

    def __init__(self, name):
        self.name = name

    def add_superpower(self, power):
        self.superpowers.append(power)


if __name__ == '__main__':
    print("=== Instance and class variables ===")
    print('# The class variable (pi) is shared by all instances of the class.')
    print('# The class variable (pi) is immutable)')
    print('# The instance variable (radio) is unique to each instance of the class.')

    print()
    print('=== Instance 1 ===')
    a = Cal(32)
    print(f'Area: {a.area()}')
    print(f'Pi: {a.pi}')
    a.pi = 43
    print(f'Pi: {a.pi}')

    print()
    print('=== Instance 2 ===')
    b = Cal(44)
    b.area()
    print(f'Area: {b.area()}')
    print(f'Pi: {b.pi}')
    b.pi = 50
    print(f'Pi: {b.pi}')

    print()
    print("=== Misuse of class and instance variables ===")
    print('# The class variable (superpowers) is shared by all instances of the class.')
    print('# The class variable (superpowers) is mutable)')
    print('# The instance variable (name) is unique to each instance of the class.')

    foo = SuperClass('foo')
    bar = SuperClass('bar')
    print(f'Foo: {foo.name}')
    print(f'Bar: {bar.name}')

    foo.add_superpower('fly')
    print(f'Foo superpowers: {foo.superpowers}')
    print(f'Bar superpowers: {bar.superpowers}')

    foo.name = 'foo2'
    print(f'Foo: {foo.name}')
    print(f'Bar: {bar.name}')

    bar.name = 'bar2'
    print(f'Foo: {foo.name}')
    print(f'Bar: {bar.name}')
