# https://python-intermedio.readthedocs.io/es/latest/collections.html

from collections import Counter

if __name__ == '__main__':
    print("=== Collections: counter ===")
    colours = (
        ('Covadonga', 'Amarillo'),
        ('Pelayo', 'Azul'),
        ('Xavier', 'Verde'),
        ('Pelayo', 'Negro'),
        ('Covadonga', 'Rojo'),
        ('Amaya', 'Plata'),
    )

    favorites = Counter(name for name, colour in colours)
    print(f'Favorites: {favorites}')
