import re


def count_words(text, words):

    counter = 0

    for word in words:
            if word in text:
                counter += 1

    return counter
