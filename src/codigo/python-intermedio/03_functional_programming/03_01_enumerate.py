# https://python-intermedio.readthedocs.io/es/latest/enumerate.html

if __name__ == '__main__':
    my_list = ['A', 'B', 'C', 'D']

    print("=== Enumerate raw ===")
    print(enumerate(my_list, 1))

    print()
    print("=== Enumerate in for ===")
    for counter, value in enumerate(my_list, 1):
        print(f'{counter}: {value}')

    print()
    print("=== Enumerate as a list ===")
    counter_list = list(enumerate(my_list, 1))
    print(counter_list)
