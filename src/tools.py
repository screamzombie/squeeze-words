import re


def init_stop_words():
    with open("../data/userData/stopWords.txt") as stop_words_file:
        stop_words = stop_words_file.read().split("\n")
    return stop_words


def get_freq_dict_by_content(content):
    stop_words = init_stop_words()
    words = re.findall(r'\w+', content.lower())
    words_clean = []
    for word in words:
        if word not in stop_words and word.isdigit() == False and len(word) > 1:
            words_clean.append(word)

    word_freq = {}
    for word in words_clean:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # sort by frequency down
    sorted_freq = sorted(
        word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq
