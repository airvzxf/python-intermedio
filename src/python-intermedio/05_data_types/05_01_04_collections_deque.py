# https://python-intermedio.readthedocs.io/es/latest/collections.html

from collections import deque

if __name__ == '__main__':
    print("=== Collections: deque ===")
    d = deque()
    d.append('1')
    d.append('2')
    d.append('3')

    print(f'Deque: {d}')
    print(f'Size: {len(d)}')
    print(f'deque[0]: {d[0]}')
    print(f'deque[-1]: {d[-1]}')

    print()
    print("=== Collections: deque using pop ===")
    d = deque(range(5))
    print(f'Deque: {d}')
    print(f'Size: {len(d)}')
    print(f'Pop left: {d.popleft()}')
    print(f'Pop: {d.pop()}')
    print(f'Deque: {d}')
    print(f'Size: {len(d)}')

    print()
    print("=== Collections: deque using max length ===")
    d = deque([0, 1, 2, 3, 5], maxlen=5)
    print(f'Deque: {d}')
    print(f'Size: {len(d)}')

    d.extend([6, 7, 8])
    print(f'Deque: {d}')
    print(f'Size: {len(d)}')

    print()
    print("=== Collections: deque using extend ===")
    d = deque([1, 2, 3, 4, 5])
    print(f'Deque: {d}')
    print(f'Size: {len(d)}')
    d.extendleft([0])
    d.extend([6, 7, 8])
    print(f'Deque: {d}')
    print(f'Size: {len(d)}')
