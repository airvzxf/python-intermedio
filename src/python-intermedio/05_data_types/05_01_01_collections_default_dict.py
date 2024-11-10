# https://python-intermedio.readthedocs.io/es/latest/collections.html

import json
from collections import defaultdict

if __name__ == '__main__':
    print("=== Collections: default dict ===")
    colours = (
        ('Asturias', 'Oviedo'),
        ('Galicia', 'Ourense'),
        ('Extremadura', 'Cáceres'),
        ('Galicia', 'Pontevedra'),
        ('Asturias', 'Gijón'),
        ('Cataluña', 'Barcelona'),
    )

    cities = defaultdict(list)

    for name, colour in colours:
        cities[name].append(colour)

    print(f'Cities: {cities}')

    print()
    print("=== Dictionary with error ===")
    some_dict = {}
    # This will raise a KeyError
    some_dict['region']['ciudad'] = "Oviedo"

    print()
    print("=== Solution ===")
    tree = lambda: defaultdict(tree)
    some_dict = tree()
    some_dict['region']['ciudad'] = "Oviedo"
    print(f'Some dict: {some_dict}')
    print(f'Some dict: {json.dumps(some_dict)}')
