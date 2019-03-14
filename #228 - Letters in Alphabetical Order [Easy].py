# https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

def letterSort(letter):
    unorderedLetter = list(())
    for char in letter:
        unorderedLetter.append(char)
    orderedLetter = unorderedLetter.copy()
    orderedLetter.sort()
    reversedLetter = unorderedLetter.copy()
    reversedLetter.sort(reverse=True)
    if unorderedLetter == orderedLetter:
        print(letter + " IN ORDER")
    elif unorderedLetter == reversedLetter:
        print(letter + " IN REVERSE ORDER")
    else:
        print(letter + " NOT IN ORDER")


wordList = ["billowy", "biopsy", "chinos", "defaced", "chintz", "sponged", "bijoux", "abhors", "fiddle", "begins",
            "chimps", "wronged"]
for word in wordList:
    letterSort(word)