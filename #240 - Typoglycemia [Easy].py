# https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/

import re
import random


def typo(sentence):
    wordList = re.findall(r'\w+', sentence)
    reworkedSentence = ""
    for word in wordList:
        newWord = ""
        newMiddle = ""
        firstLetter = word[0]
        middleLetters = word[1:(len(word)-1)]
        middleList = list(middleLetters)
        random.shuffle(middleList)
        for char in middleList:
            newMiddle += char
        lastLetter = word[-1]
        newWord += firstLetter
        newWord += newMiddle
        newWord += lastLetter
        reworkedSentence += newWord + " "
    print(reworkedSentence)


typo("According to a research team at Cambridge University, " +
     "it doesn't matter in what order the letters in a word are, the only important thing is that the first and last letter be in the right place. " +
    "The rest can be a total mess and you can still read it without a problem." +
    "This is because the human mind does not read every letter by itself, but the word as a whole. " +
    "Such a condition is appropriately called Typoglycemia.")

