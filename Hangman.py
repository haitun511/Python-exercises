import random
from urllib import request
from bs4 import BeautifulSoup

url = "http://www-personal.umich.edu/~jlawler/wordlist"
with request.urlopen(url) as response:
    soup = BeautifulSoup(response, "lxml")

word_list = []
words = soup.get_text().split()

for word in words:
    word_list.append(word)

guess_word = random.choice(word_list)
print("This word has {} letters.".format(len(guess_word)))

counter = 0
max_guess = 15
tried_letter = []

while counter < max_guess:
    current_guess = input("Guess a letter ({} guess remaining): ".format(str(max_guess - counter)))
    tried_letter.append(current_guess)

    if current_guess in list(guess_word):
        print("Nice guess!")
    else:
        print("Nice try but this letter is not included!")

    show_word = []
    for letter in list(guess_word):
        if letter in tried_letter:
            show_word.append(letter)
        else:
            show_word.append("?")

    if not "?" in show_word:
        print("You are a genius! The word is {}.".format("".join(show_word)))
        exit()

    print("".join(show_word))
    counter += 1

print("Sorry but you didn't make it! The word is {}.".format(guess_word))
