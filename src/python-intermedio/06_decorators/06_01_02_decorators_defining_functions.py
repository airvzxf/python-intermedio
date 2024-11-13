# https://python-intermedio.readthedocs.io/es/latest/decorators.html

def hi():
    print("You are inside the hi() function")

    def greet():
        return "You are inside the greet() function"

    def welcome():
        return "You are inside the welcome() function"

    print(greet())
    print(welcome())
    print("Back to the hi() function")


if __name__ == '__main__':
    hi()
    # This shows how every time you call the hi() function
    # It is actually also called greet() and welcome()
    # However, these last two functions are not accessible
    # outside of hi(). If we try that, we will get an error.

    # This will give a NameError.
    greet()
