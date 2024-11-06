# https://python-intermedio.readthedocs.io/es/latest/for_-_else.html

if __name__ == '__main__':
    print('=== Common For ===')
    fruits = ['apple', 'banana', 'mango']
    for fruit in fruits:
        print(fruit.capitalize())

    print()
    print('=== For with break ===')
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equal', x, '*', n / x)
                break

    print()
    print('=== For/Else ===')
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equal', x, '*', n / x)
                break
        else:
            print(n, 'it is a prime number')
