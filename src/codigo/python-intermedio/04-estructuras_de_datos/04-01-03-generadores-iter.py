# https://python-intermedio.readthedocs.io/es/latest/generators.html

if __name__ == '__main__':
    my_string = "Hello"

    # This is not a generator.
    print("=== Extract letters as a list ===")
    print(my_string[0])
    print(my_string[1])
    print(my_string[2])
    print(my_string[3])

    # This is not a generator.
    print()
    print("=== Iterating over a string with For ===")
    for letter in my_string:
        print(letter)

    # STEP 1: Uncomment the below code.
    # The following line will raise a TypeError exception.
    # next(my_string)

    # STEP 2: Show the iteration for the string variable.
    print()
    print("=== Iterating over a string with Iter and Next ===")
    my_iter = iter(my_string)
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

    # STEP 3: Uncomment the below code.
    # The following line will raise a TypeError exception.
    # number = 1779
    # iter(number)
