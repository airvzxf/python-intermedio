# https://python-intermedio.readthedocs.io/es/latest/collections.html

from collections import namedtuple
from enum import Enum


class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    wolf = 4
    butterfly = 5
    owl = 6
    # And many more!

    # Aliases can also be used
    little_cat = 1
    little_dog = 2


if __name__ == '__main__':
    print("=== Enum ===")
    animal = namedtuple('Animal', 'name age type')
    print(f'Animal type: {type(animal)}')
    print(f'Animal: {animal}')
    perry = animal(name="Perry", age=31, type=Species.cat)
    horse = animal(name="HorseLuis", age=4, type=Species.horse)
    tom = animal(name="Tom", age=75, type=Species.wolf)
    luna = animal(name="Luna", age=35, type=Species.little_cat)
    print(f'Perry: {perry}')
    print(f'Horse: {horse}')
    print(f'Tom: {tom}')
    print(f'Luna: {luna}')

    print()
    print('=== Access to the enum ===')
    print(f'Species(1): {Species(1)}')
    print(f'Species[cat]: {Species["cat"]}')
    print(f'Species.cat: {Species.cat}')
