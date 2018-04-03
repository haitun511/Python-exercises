import string


def check(data):

    lst = sorted(data.lower())
    letters = []

    for letter in lst:
        if letter.isalpha():
            letters.append(letter)

    most_wanted_letter = letters[0]
    counter = 1
    max_count = 1

    if len(letters) > 1:
        for i in range(1,len(letters)-1):
            if letters[i] != letters[i-1]:
                counter = 1
            else:
                counter += 1
                if counter > max_count:
                    max_count = counter
                    most_wanted_letter = letters[i]

    print(most_wanted_letter)


check("q????")