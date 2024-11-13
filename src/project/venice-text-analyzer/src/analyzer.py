import argparse
import os
import re

from utils import tokenize_text, count_words, count_unique_words, count_word_frequency
from visualizer import visualize_word_frequency


def analyze_text(file_path, search_words=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        tokens = tokenize_text(text)
        words = [word.lower() for word in tokens]

    if search_words:
        search_words = [word.lower() for word in search_words]
        word_frequency = count_word_frequency(words, search_words)
        print(f'Frequency of search words:')
        for word, freq in word_frequency.items():
            print(f'{word}: {freq}')

    word_count = count_words(words)
    unique_word_count = count_unique_words(words)
    print(f'Word count: {word_count}')
    print(f'Unique word count: {unique_word_count}')

    if unique_word_count > 0:
        visualize_word_frequency(words, os.path.join('..', 'data', 'stopwords.txt'))


def main():
    parser = argparse.ArgumentParser(description='Text Analyzer')
    parser.add_argument('file_path', type=str, help='Path to the text file')
    parser.add_argument('--search-words', nargs='+', type=str, help='Search for frequency of specific words')
    args = parser.parse_args()

    analyze_text(args.file_path, args.search_words)


if __name__ == '__main__':
    main()
