import random

from colorama import Fore, Back, Style


def guess_the_word():
    get_out_of_game = False
    while not get_out_of_game:
        list_of_words = ["react", "later", "about", "paint", "anime", "tired", "right", "shine", "quiet", "whose",
                         "yeast", "dream", "guard", "adult", "sight", "force", "brave", "cable", "panic", "study",
                         "faith", "equal", "grade", "voice", "drive", "alert", "third", "first", "actor", "begin",
                         "chime", "clean", "diner", "feast", "flame", "globe", "grain", "heart", "hindu", "intel",
                         "joker", "lower", "lunar", "mercy", "noisy", "noise", "vague", "bacon"]
        word = random.choice(list_of_words)
        answer_from_user = ""
        i = 0
        while i < 4 and answer_from_user != word:
            i += 1
            answer_from_user = input("Guess a word that is 5 letters.")
            while len(answer_from_user) != 5:
                print("That's not 5 letters!")
                answer_from_user = input("Guess a word that is 5 letters.")
            letter = ""
            for index in range(len(answer_from_user)):
                # Red, not in word, Yellow, in word but not in right place, Green, In the word and the right spot.
                if word.find(answer_from_user[index]) < 0:
                    letter += (Fore.RED + answer_from_user[index])
                else:
                    if index == word.find(answer_from_user[index], index):
                        letter += (Fore.GREEN + answer_from_user[index])
                    else:
                        letter += (Fore.YELLOW + answer_from_user[index])
            print(letter)
            print(Fore.RESET)
        if answer_from_user == word:
            print("Congratulations! You got the correct answer! :D")
        else:
            print("Wrong answer! The correct answer was " + word + ".")
        try_again = input("Do you want to try it again?")
        if try_again == "no":
            get_out_of_game = True


if __name__ == "__main__":
    print(Style.RESET_ALL)
    guess_the_wordimport random

    get_out_of_game = False
        answer_from_user = ""
        i = 0
        while i < 4 and answer_from_user != word:
            i += 1
            answer_from_user = input("Guess a word that is 5 letters.")
            while len(answer_from_user) != 5:
                print("That's not 5 letters!")
                answer_from_user = input("Guess a word that is 5 letters.")
            letter = ""
            for index in range(len(answer_from_user)):
                # Red, not in word, Yellow, in word but not in right place, Green, In the word and the right spot.
                if word.find(answer_from_user[index]) < 0:
                    letter += (Fore.RED + answer_from_user[index])
                else:
                    if index == word.find(answer_from_user[index], index):
                        letter += (Fore.GREEN + answer_from_user[index])
                    else:
                        letter += (Fore.YELLOW + answer_from_user[index])
            print(letter)
            print(Fore.RESET)
        if answer_from_user == word:
            print("Congratulations! You got the correct answer! :D")
        else:
            print("Wrong answer! The correct answer was " + word + ".")
        try_again = input("Do you want to try it again?")
        if try_again == "no":
            get_out_of_game = True


if __name__ == "__main__":
    print(Style.RESET_ALL)
    guess_the_word()
