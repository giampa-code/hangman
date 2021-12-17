# Hangman game

# func for reading all the words in the data.txt
import random
import os

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

# print the list with the word in the specified format
def print_incompleted_word(word_letters_list):
    print(' '.join((word_letters_list)))

# refresh the uncompleted word with the new letters
def refresh_letters(word,to_complete_word,letter):
    """
    Given a letter, compare if that letter is in the original word
    and if true, refresh it in the 'to complete' word
    """
    positions = [pos for pos, char in enumerate(word) if char == letter]
    for i in positions:
        to_complete_word[i] = letter
    return to_complete_word

# clear the screen and print the new screen
def clean_and_print(to_complete_word, used_letters, flag, lives):
    """
    t_c_w = list, u_l = set, flag = number, lives = number
    """
    # clear the screen
    os.system("clear")
    # print the new screen
    print_incompleted_word(to_complete_word)
    print("\n")
    print(f"Remaining lives: {lives}")
    if flag == 0:
        print("Correct letter!")
        print("\n")
        print(f"Already used letters: \n{used_letters}")
        print("\n")
    elif flag == 1:
        print("Letter already used. Try with a new one.")
        print("\n")
        print(f"Already used letters: \n{used_letters}")
        print("\n")
    elif flag == 2:
        print("Incorrect letter. Try again!")
        print("\n")
        print(f"Already used letters: \n{used_letters}")
        print("\n")
    elif flag == 3:
        # clear the screen
        os.system("clear")
        print_incompleted_word(to_complete_word)
        print("\n")
        print("You win!")
    elif flag == 4:
        # clear the screen
        os.system("clear")
        print_incompleted_word(to_complete_word)
        print("\n")
        print("You lost!") 
    elif flag == 10:
        print("Only one letter is allowed.")
        print("\n")
        print(f"Already used letters: \n{used_letters}")
        print("\n")

# play again function
def play_again():
    while True:
        try:
            again = input("Play again? [y/n] \n")
            if again != 'y' and again !='n':
                raise ValueError("Only letters are allowed")
            if again == 'y':
                return True
            elif again == 'n':
                return False
        except ValueError:
            print("Valid inputs: y or n")

def run():
    # Starting the outer loop
    while True:
        # create the list with the words
        words = read()
        # choose a random word
        random_word = choose_random_word(words)
        # create a list with n "_" with n=len(random_word)
        to_complete_word = ["_" for i in range(len(random_word))]

        # set with the used letters
        used_letters = set()

        # numbers of lives
        lives = 6
        # letter flag for the clean and print func
        print_flag = -1    

        # game loop
        while True:
            
            # if to_complete_letter == random word, the player wins
            # .join to conver list into string
            if "".join(to_complete_word) == random_word:
                print_flag = 3
                clean_and_print(to_complete_word, used_letters, print_flag, lives)
                break
            # if lives >= max lives, player lose
            if lives <= 0:
                print_flag = 4
                clean_and_print(to_complete_word, used_letters, print_flag, lives)
                break
            
            # clean and print screen
            clean_and_print(to_complete_word, used_letters, print_flag, lives)

            # enter a letter and test if it is in the random word.
            # if true, refresh it in the 'to complete word'
            # if false, add to the used letters set and subtract a life
            try:
                letter = input("Enter a letter: ")
                if not letter.isalpha() or not len(letter)==1:
                    raise ValueError("Only letters are allowed")
                if letter in random_word:
                    # refresh the letter in the tcw list
                    to_complete_word = refresh_letters(random_word, to_complete_word, letter)
                    # flag to 0 to print "correct letter!"
                    print_flag = 0
                elif letter in used_letters:
                    # letter flag 1 to print "letter already used"
                    print_flag = 1
                else:
                    lives -= 1
                    # flag to 2 to print "Incorrect letter!"
                    print_flag = 2 
                used_letters.add(letter)
            
            # error if input is not letter
            except ValueError:
                # flag to 10 to print "only one letter is allowed"
                print_flag = 10

        # if player wins
        if print_flag == 3:
            #play again: continue
            if play_again():
                continue
            #not play again: break
            else:
                break


        # if player lose
        if print_flag == 4:
            # play again: continue
            if play_again():
                continue
            # not play again: break
            else:
                break


# run main func
if __name__ == '__main__':
    run()