# https://www.reddit.com/r/dailyprogrammer/comments/45w6ad/20160216_challenge_254_easy_atbash_cipher/

import string


def initAlphabetDict():
    i = 1
    alphabetBook = dict()
    for alphabet in string.ascii_lowercase:
        alphabetBook[i] = alphabet
        i += 1
    print(alphabetBook)
    return alphabetBook


def encrypt(line):
    alphabets = initAlphabetDict()
    lineList = list(line)
    encryptedString = ""
    x = ' '
    print(lineList)
    for char in lineList:
        if char == ' ':
            encryptedString += x
        for currKey, alphabet in alphabets.items():
            if char is alphabet:
                newChar = alphabets[27 - currKey]
                encryptedString += newChar
    print(encryptedString)


encrypt('foobar')