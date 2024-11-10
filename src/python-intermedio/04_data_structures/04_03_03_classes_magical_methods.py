# https://python-intermedio.readthedocs.io/es/latest/classes.html

class GetTest(object):
    def __init__(self, name):
        print(f'Greetings {name}!!')
        self.info = {
            'name': 'Cordovan',
            'country': 'Asturias',
            'number': 12345812
        }

    @staticmethod
    def another_method():
        print('I am another method that is not called'
              ' automatically')

    def __getitem__(self, i):
        return self.info[i]


if __name__ == '__main__':
    print("=== Magical methods ===")
    a = GetTest('Kassia')
    a.another_method()

    print()
    print(f'Name: {a["name"]}')
    print(f'Country: {a["country"]}')
    print(f'Number: {a["number"]}')
