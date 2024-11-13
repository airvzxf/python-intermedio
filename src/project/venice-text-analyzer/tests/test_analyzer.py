import unittest

from ..src.analyzer import analyze_text


class TestAnalyzer(unittest.TestCase):
    def test_analyze_text(self):
        file_path = '../data/sample.txt'
        search_words = ['lorem', 'ipsum']
        analyze_text(file_path, search_words)


if __name__ == '__main__':
    unittest.main()
