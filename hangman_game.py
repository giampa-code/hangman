# Hangman game

# func for reading all the words in the data.txt
import random


def read():
    import unidecode
    words = []
    with open('./data/data.txt','r', encoding='utf-8') as f:
        # add this line to prevent reading the newlines '\n' after each word
        file = f.read().splitlines()
        # add every word in the file to a list
        for line in file:
            # Using unidecode library to replace special characters from vowels
            words.append(unidecode.unidecode(line))
    return words
# func for selecting a random word
def choose_random_word(words):
    import random
    return random.choice(words)

def run():
    # create the list with the words
    words = read()
    # choose a random word
    random_word = choose_random_word(words)
    print(random_word)

if __name__ == '__main__':
    run()