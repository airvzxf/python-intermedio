# https://python-intermedio.readthedocs.io/es/latest/collections.html

from collections import OrderedDict

if __name__ == '__main__':
    print("=== Without ordered dict ===")
    print('The order of the elements is not guaranteed')
    colours = {"Rojo": 198, "Verde": 170, "Azul": 160}
    for key, value in colours.items():
        print(key, value)

    print()
    print("=== Collections: ordered dict ===")
    print('The order of the elements is guaranteed')
    colours = OrderedDict([("Rojo", 198), ("Verde", 170), ("Azul", 160)])
    for key, value in colours.items():
        print(key, value)
