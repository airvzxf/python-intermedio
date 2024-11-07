# https://python-intermedio.readthedocs.io/es/latest/generators.html

from resource import getrusage, RUSAGE_SELF
from time import sleep


def fibonacci_yield(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci_return(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def using(point=''):
    usage = getrusage(RUSAGE_SELF)
    return (f'{point}'
            f' | User-time: {usage[0]:.5f}'
            f' | Sys-time: {usage[1]:.5f}'
            f' | Mem: {(usage[2] / 1024.0):,.2f} mb')


if __name__ == '__main__':
    target = 1000000
    # STEP 1: Execute the Fibonacci function with Yield.
    sleep(1)
    print("=== Fibonacci Yield ===")
    print(using("Before"))
    for number in fibonacci_yield(target):
        number += 0
    print(using("After "))

    # STEP 2: Execute the Fibonacci function with Return.
    sleep(2)
    print()
    print("=== Fibonacci Return ===")
    print(using("Before"))
    for number in fibonacci_return(target):
        number += 0
    print(using("After "))

    # STEP 3: Compare the results and explain the differences of the RAM.
