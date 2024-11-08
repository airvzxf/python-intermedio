# https://python-intermedio.readthedocs.io/es/latest/set_-_data_structure.html

if __name__ == '__main__':
    abc_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

    print("=== Duplicated with For statement ===")
    duplicated = []
    for value in abc_list:
        if abc_list.count(value) > 1:
            if value not in duplicated:
                duplicated.append(value)
    print(f'Duplicated values: {duplicated}')

    print()
    print("=== Duplicated with Set and Lambdas ===")
    duplicated = set([x for x in abc_list if abc_list.count(x) > 1])
    print(f'Duplicated values: {duplicated}')

    print()
    print("=== Set using {} ===")
    set_1 = {'red', 'blue', 'green'}
    print(f'Type of set_1: {type(set_1)} | {set_1}')

    set_1 = {'yellow', 'red', 'blue', 'green', 'black'}
    set_2 = {'red', 'brown'}

    print()
    print("=== Intersection ===")
    print(f'Intersection between set_1 and set_2: {set_1.intersection(set_2)}')

    print()
    print("=== Difference ===")
    print(f'Difference between set_1 and set_2: {set_1.difference(set_2)}')
