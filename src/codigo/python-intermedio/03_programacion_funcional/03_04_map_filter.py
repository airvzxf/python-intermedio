# https://python-intermedio.readthedocs.io/es/latest/map_filter.html

from functools import reduce


def multiplication(x):
    return x * x


def sum_number(x):
    return x + x


if __name__ == '__main__':
    print('=== Squared with For ===')
    numbers = [1, 2, 3, 4, 5]
    squared = []
    for i in numbers:
        squared.append(i ** 2)
    print(f'Squared: {squared}')

    print()
    print('=== Squared with Map Function ===')
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f'Squared: {squared}')

    print()
    print('=== Map Function with functions ===')
    functions = [multiplication, sum_number]
    for i in range(5):
        valor = list(map(lambda x: x(i), functions))
        print(valor)

    print()
    print('=== Filter Function ===')
    list_numbers = range(-5, 5)
    less_zero = list(filter(lambda x: x < 0, list_numbers))
    print(f'Less than zero: {less_zero}')

    print()
    print('=== Filter Function ===')
    numbers = [1, 2, 3, 4, 5]
    even = list(filter(lambda x: x % 2 == 0, numbers))
    print(f'Even numbers: {even}')

    print()
    print('=== Without Reduce ===')
    product = 1
    lista = [1, 2, 3, 4]
    for num in lista:
        product = product * num
    print(f'Product: {product}')

    print()
    print('=== Reduce ===')
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print(f'Product: {product}')
