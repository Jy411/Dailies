# https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

import random


def wordGenerator(cv):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    string = list(cv)
    newString = ""
    for character in string:
        if character == 'c':
            newString += random.choice(consonants)
        elif character == 'C':
            newString += (random.choice(consonants)).upper()
        elif character == 'v':
            newString += random.choice(vowels)
        elif character == 'V':
            newString += (random.choice(vowels)).upper()
    print(newString)


userInput = input("Enter a string(c and v): ")
wordGenerator(userInput)