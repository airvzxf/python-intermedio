# https://python-intermedio.readthedocs.io/es/latest/collections.html

from collections import namedtuple

if __name__ == '__main__':
    print("=== Tuple ===")
    man = ('Joe', 30)
    print(f'Name: {man[0]} | Age: {man[1]}')

    print()
    print("=== Collections: named tuple ===")
    animal = namedtuple('Animal', 'name age type')
    perry = animal(name="Perry", age=31, type="cat")
    print(f'Animal: {animal}')
    print(f'Perry: {perry}')
    print(f'Perry name: {perry.name}')

    print()
    print("=== Named tuple is immutable ===")
    # This throws an AttributeError.
    # perry.age = 42
    print(f'Perry age: {perry.age}')

    print()
    print("=== Named tuple is indexable ===")
    print(f'Perry[0]: {perry[0]}')

    print()
    print("=== Named tuple converted to Dict ===")
    perry_dict = perry._asdict()
    print(f'Perry dict: {perry_dict}')
