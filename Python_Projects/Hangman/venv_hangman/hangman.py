from word_list import word as w
import string
import random

no_of_turns = 8
def get_word():
    selected_word = random.choice(w)
    return selected_word.lower()

def display_word(word, used_letters):
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print("Current Word:\n", ' '.join(word_list))

def play():
    word = get_word()
    letters_in_word = set(word) #Unique letter in a word
    used_letters = set() # What user guessd unique letters
    alphabet = set(string.ascii_lowercase)
    global  no_of_turns
    print(f"You have {no_of_turns} lives")

    while len(letters_in_word) > 0 and no_of_turns > 0:
        display_word(word, used_letters)
        print("You have used the these letters", ' '.join(used_letters))
        print("Remaining lives:" + str(no_of_turns))
        user_letter = input("Guess the Word, input a letter:").lower()


        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_in_word:
                letters_in_word.remove(user_letter)
            else:                
                no_of_turns = no_of_turns -1
                print("Incorect guess remaining lives:" + str(no_of_turns))
        elif user_letter in used_letters:
            print("You already guessed the same letter")
        else:
            print("Please try again, Invalid Character.")

    if(no_of_turns > 0):
        print("You have guessed correctly",word)

play()