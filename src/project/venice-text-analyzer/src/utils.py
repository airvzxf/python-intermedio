import nltk


def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def count_words(words):
    return len(words)


def count_unique_words(words):
    unique_words = set(words)
    return len(unique_words)


def count_word_frequency(words, search_words):
    word_frequency = {}
    for word in search_words:
        word_frequency[word] = words.count(word)
    return word_frequency
