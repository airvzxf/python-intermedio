def single_argument(arg):
    print("=== Single argument ===")
    print(f'arg: {arg}')
    print()


def multiple_arguments(*args):
    print("=== Multiple arguments ===")
    print(f'args: {args}')
    print()


# STEP 2: Change the name of the argument in the function: kwargs to blablabla.
def multiple_keyword_arguments(**kwargs):
    print("=== Multiple keyword arguments ===")
    print(f'kwargs: {kwargs}')
    print()


def args_kwargs(*args, **kwargs):
    print("=== Arguments and keyword arguments ===")
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print()


def arg_args_kwargs(arg, *args, **kwargs):
    print("=== Argument, arguments and keyword arguments ===")
    print(f'arg: {arg}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print()


def equivalent_to_args_kwargs(args, kwargs):
    print("=== Equivalent to args and kwargs ===")
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print()


if __name__ == '__main__':
    # STEP 1: Execute the file and explain the below sentences.
    single_argument('Hello')
    multiple_arguments('Hello', 'World')
    # STEP 2: Change the name of the argument in the function: kwargs to blablabla.
    multiple_keyword_arguments(first='Hello', second='World')
    args_kwargs('Hello', 'World', first='Hello', second='World')
    arg_args_kwargs('O.O', 'Hello', 'World', first='Hello', second='World')

    # STEP 3: Explain the most common use of multiple values sent through the function.
    my_args = ('Hello', 'World')
    my_kwargs = {'first': 'Hello', 'second': 'World'}
    equivalent_to_args_kwargs(my_args, my_kwargs)

    # STEP 4: Explain where useful the *args and **kwargs are.
