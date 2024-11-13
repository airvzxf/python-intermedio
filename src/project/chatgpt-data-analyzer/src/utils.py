from csv import DictReader


def load_data(file_path):
    """Carga datos desde un archivo CSV"""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        return list(DictReader(csvfile))
