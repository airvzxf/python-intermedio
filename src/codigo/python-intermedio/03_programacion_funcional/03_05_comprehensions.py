# https://python-intermedio.readthedocs.io/es/latest/comprehensions.html

if __name__ == '__main__':
    print('=== Squared without comprehension ===')
    squared = []
    for x in range(10):
        squared.append(x ** 2)
    print(f'Squared: {squared}')

    print()
    print('=== Squared with comprehension ===')
    squared = [x ** 2 for x in range(10)]
    print(f'Squared: {squared}')

    print()
    print('=== Comprehension List ===')
    multiples = [i for i in range(30) if i % 3 == 0]
    print(f'Multiples of 3: {multiples}')

    print()
    print('=== Comprehension Dict ===')
    m_case = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

    m_case_frequency = {
        k.lower(): m_case.get(k.lower(), 0) + m_case.get(k.upper(), 0)
        for k in m_case.keys()
    }
    print(f'Frequency: {m_case_frequency}')

    print()
    print('=== Comprehension Dict ===')
    m_case_inverted = {v: k for k, v in m_case.items()}
    print(f'Inverted keys and values: {m_case_inverted}')

    print()
    print('=== Comprehension Set ===')
    squared = {x ** 2 for x in [1, 1, 2]}
    print(f'Squared: {squared}')

    print()
    print('=== Comprehension generator ===')
    multiples_gen = (i for i in range(30) if i % 3 == 0)
    print(f'Multiples generator: {multiples_gen}')
    for number in multiples_gen:
        print(f'Number: {number}')
