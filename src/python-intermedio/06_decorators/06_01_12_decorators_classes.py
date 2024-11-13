# https://python-intermedio.readthedocs.io/es/latest/decorators.html

from functools import update_wrapper


class Logit(object):
    _logfile = 'test-07.log'

    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args):
        # We write the log (see method).
        self.logging()
        # We send a notification (see method).
        self.notify()

        # Returns the base function
        return self.func(*args)

    def logging(self):
        print(f'Logging in the file {self._logfile}')
        log_string = f'Logging: {self.func.__name__} was called'
        print(log_string)
        # Open the log file and write
        with open(self._logfile, 'a') as opened_file:
            # We write the content
            opened_file.write(log_string + '\n')

    def notify(self):
        # This class simply writes the log, nothing else.
        print(f'Notify: {self.func.__name__} was called')


class EmailLogit(Logit):
    """
    Implementing logit with email sending
    """

    def __init__(self, func, email='admin@my-project.com', *args, **kwargs):
        self.email = email
        super(EmailLogit, self).__init__(func)

    def notify(self):
        # We send email to self.email
        # Code to send email
        # ...
        print(f'Sent email from {self.email}')
        print(f'Sent email: {self.func.__name__} was called')


@Logit
def my_func_1():
    print('Working in my_func_1')


@EmailLogit
def my_func_2():
    print('Working in my_func_2')


if __name__ == '__main__':
    print('=== Decorating classes ===')
    my_func_1()

    print()
    print('=== Change log file ===')
    # If we want to use another name
    Logit._logfile = 'test-08.log'
    my_func_1()

    print()
    print('=== Function __name__ ===')
    # It will raise an AttributeError if not use update_wrapper.
    print(f'my_func_1.__name__: {my_func_1.__name__}')

    print()
    print('=== Inherited class with decorator ===')
    my_func_2()
