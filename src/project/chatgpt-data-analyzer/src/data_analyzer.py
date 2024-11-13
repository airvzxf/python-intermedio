from collections import Counter
from enum import Enum
from functools import lru_cache

from .decorators import timing


class Categoria(Enum):
    TIPO_A = "Tipo A"
    TIPO_B = "Tipo B"


class DataAnalyzer:
    __slots__ = ['data']

    def __init__(self, data):
        self.data = data

    @timing
    def count_categories(self):
        return Counter(row['category'] for row in self.data)

    @timing
    @lru_cache(maxsize=32)
    def calculate_average(self, field):
        total = sum(float(row[field]) for row in self.data if row[field])
        return total / len(self.data)

    def filter_data(self, **kwargs):
        filtered_data = self.data
        for key, value in kwargs.items():
            filtered_data = [row for row in filtered_data if row.get(key) == value]
        return filtered_data
