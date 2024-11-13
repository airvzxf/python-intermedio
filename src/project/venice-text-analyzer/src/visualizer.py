import matplotlib.pyplot as plt
from nltk.corpus import stopwords


def visualize_word_frequency(words, stopwords_filepath):
    stop_words = set(stopwords.words('english'))
    with open(stopwords_filepath, 'r', encoding='utf-8') as file:
        stop_words.update(file.read().splitlines())

    word_counts = {}
    for word in words:
        if word.lower() not in stop_words:
            if word.lower() in word_counts:
                word_counts[word.lower()] += 1
            else:
                word_counts[word.lower()] = 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_word_counts[:10]

    labels, values = zip(*top_words)
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.title('Top 10 Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()
