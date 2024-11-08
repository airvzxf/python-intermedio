# https://python-intermedio.readthedocs.io/es/latest/coroutines.html

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def grep(pattern):
    print(f'Searching: {pattern}')
    while True:
        line = (yield)
        if pattern in line:
            print(f'Found: {line}')
        else:
            print(f'Not found: {line}')


if __name__ == '__main__':
    print("=== Fibonacci generator infinite ===")
    for i in fibonacci():
        print(f'Fibonacci: {i}')
        # If this condition is not met, the loop will never end.
        if i > 5:
            break

    print()
    print("=== Coroutine ===")
    search = grep('coroutine')
    print(f'Search: {search}')
    next(search)
    print(f'Search: {search}')
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutines instead!")
    search.close()
