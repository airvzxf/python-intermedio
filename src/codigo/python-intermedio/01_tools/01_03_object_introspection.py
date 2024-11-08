# https://python-intermedio.readthedocs.io/es/latest/object_introspection.html

from inspect import getmembers

if __name__ == '__main__':
    # STEP 1: Show the methods and attributes of a list.
    my_list = [15, 3, 9]
    print("=== Dir ===")
    print(f'Methods and attributes of my list: {dir(my_list)}')

    # STEP 2: Show the method sort.
    # Show the list and then sort the list and show again.
    print(f'Unsorted list: {my_list}')
    my_list.sort()
    print(f'Sorted list: {my_list}')

    print()
    print("=== Type ===")
    print(f'String: {type('')}')
    print(f'List: {type([])}')
    print(f'Dict: {type(dict)}')
    print(f'Int: {type(8)}')
    print(f'Float: {type(3.1416)}')

    print()
    print("=== Id ===")
    nombre = "Ashley"
    print(f'Name: {nombre}')
    print(f'Memory address: 0x{id(nombre):x} ({id(nombre)})')
    print('---')
    nombre = "Britany"
    print(f'Name: {nombre}')
    print(f'Memory address: 0x{id(nombre):x} ({id(nombre)})')
    print('---')
    nombre = "Britany"
    print(f'Name: {nombre}')
    print(f'Memory address: 0x{id(nombre):x} ({id(nombre)})')
    print('------')
    number = 123
    print(f'Number: {number}')
    print(f'Memory address: 0x{id(number):x}')
    print('---')
    number = 123
    print(f'Number: {number}')
    print(f'Memory address: 0x{id(number):x}')
    print('------')
    nombre = "Britany"
    print(f'Name: {nombre}')
    print(f'Memory address: 0x{id(nombre):x}')

    print()
    print("=== Inspect module ===")
    print(f'My list: {getmembers(my_list)}')
    print(f'String: {getmembers(str)}')
