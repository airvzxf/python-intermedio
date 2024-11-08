# https://python-intermedio.readthedocs.io/es/latest/global_&_return.html

def profile_global():
    global name_global
    global age_global
    name_global = "Kim"
    age_global = 27


def profile_multiple_return():
    nombre = "Selene"
    edad = 30
    return nombre, edad


if __name__ == '__main__':
    print('=== Global variables ===')
    profile_global()
    print(f'Name global: {name_global} | Age global: {age_global}')

    print()
    print('=== Multiple returns and show as a tuple ===')
    profile_data = profile_multiple_return()
    print(f'Name[0]: {profile_data[0]} | Age[0]: {profile_data[1]}')

    print()
    print('=== Multiple returns and assign into the variables ===')
    name_global, age_global = profile_multiple_return()
    print(f'Name: {name_global} | Age: {age_global}')
