# https://python-intermedio.readthedocs.io/es/latest/function_caching.html

from functools import lru_cache
from time import time


@lru_cache(maxsize=32)
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    repeat = 36

    print('=== Fibonacci with cache ===')
    fibonacci_cache.cache_clear()
    start_time = time()
    fibonacci_numbers = [fibonacci_cache(n) for n in range(repeat)]
    end_time = time()
    time_lapse = end_time - start_time
    print(f'Time lapse with cache: {time_lapse:.20f} seconds')
    print(f'Fibonacci numbers ({len(fibonacci_numbers)}): {fibonacci_numbers}')

    print()
    print('=== Fibonacci with cache reversed ===')
    fibonacci_cache.cache_clear()
    start_time = time()
    fibonacci_numbers = [fibonacci_cache(n) for n in range(repeat - 1, -1, -1)]
    end_time = time()
    time_lapse = end_time - start_time
    print(f'Time lapse with cache: {time_lapse:.20f} seconds')
    print(f'Fibonacci numbers ({len(fibonacci_numbers)}): {fibonacci_numbers}')

    print()
    print('=== Fibonacci without cache ===')
    start_time = time()
    fibonacci_numbers = [fibonacci(n) for n in range(repeat)]
    end_time = time()
    time_lapse = end_time - start_time
    print(f'Time lapse without cache: {time_lapse:.20f} seconds')
    print(f'Fibonacci numbers ({len(fibonacci_numbers)}): {fibonacci_numbers}')

    fibonacci_cache.cache_clear()
