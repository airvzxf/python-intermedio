# https://python-intermedio.readthedocs.io/es/latest/lambdas.html

if __name__ == '__main__':
    print("=== Lambdas ===")
    result = lambda x, y: x + y
    print(f'Lambda result: {result(2, 3)}')

    print()
    print("=== Sort a list by second value ===")
    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    print(f'Original list: {a}')
    a.sort(key=lambda x: x[1])
    print(f'Sorted list: {a}')

    print()
    print("=== Sort lists in parallel by first list ===")
    list_1 = [8, 95, 2, 38]
    list_2 = [99, 75, 55, 1]
    print(f'List 1: {list_1}')
    print(f'List 2: {list_2}')
    data = list(zip(list_1, list_2))
    data.sort()
    list_sorted_1, list_sorted_2 = map(lambda t: list(t), zip(*data))
    print(f'Sorted list 1: {list_sorted_1}')
    print(f'Sorted list 2: {list_sorted_2}')
