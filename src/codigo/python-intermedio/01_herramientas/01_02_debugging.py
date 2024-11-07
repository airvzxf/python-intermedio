# https://python-intermedio.readthedocs.io/es/latest/debugging.html

import pdb


def do_something(name):
    # STEP 3: Add a breakpoint in line 1 of the function do_something.
    pdb.set_trace()
    # breakpoint()
    return f"I don't want to do anything, {name}"


if __name__ == '__main__':
    # STEP 1: Execute the file and explain the below sentences.
    my_name = "Genaro"
    # STEP 2: Add a breakpoint in line 1 of the function do_something.
    print(do_something(my_name))
