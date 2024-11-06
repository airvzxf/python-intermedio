# https://python-intermedio.readthedocs.io/es/latest/generators.html

def generating_function():
    for i in range(3):
        yield i


if __name__ == '__main__':
    generator = generating_function()
    print(f'1st call: {next(generator)}')
    print(f'2nd call: {next(generator)}')
    print(f'3rd call: {next(generator)}')
    # The following line will raise a StopIteration exception.
    print(f'4th call: {next(generator)}')
