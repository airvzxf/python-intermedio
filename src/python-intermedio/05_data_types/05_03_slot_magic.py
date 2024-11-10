# https://python-intermedio.readthedocs.io/es/latest/__slots__magic.html

class MyClassWithoutSlots(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class MyClassWithSlots(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


if __name__ == '__main__':
    print('=== Without __slots__ ===')
    obj1 = MyClassWithoutSlots('Axe', 1)
    print(obj1)
    print(f'__dict__: {obj1.__dict__}')
    print(f'Name: {obj1.name}')
    print(f'Identifier: {obj1.identifier}')

    print()
    print("=== Magical method __slots__ ===")
    obj2 = MyClassWithSlots('Woo', 1)
    print(obj2)
    print(f'__slots__: {obj2.__slots__}')
    print(f'Name: {obj2.name}')
    print(f'Identifier: {obj2.identifier}')
