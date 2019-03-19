# https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/
# Did not do bonuses


def scrabble(rackTiles, controlWord):
    rackTiles = list(rackTiles)
    controlWord = list(controlWord)
    constructedWord = list()
    for letter in controlWord:
        for tile in rackTiles:
            if letter == tile:
                constructedWord.append(letter)
                rackTiles.remove(tile)
    controlWord = ''.join(controlWord)
    constructedWord = ''.join(constructedWord)
    if controlWord == constructedWord:
        print('true')
    else:
        print('false')


scrabble("orrpgma", "program")