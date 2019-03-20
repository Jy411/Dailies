# https://old.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/


def tally(scoreTrack):
    scoreTrack = list(scoreTrack)
    print(scoreTrack)
    scoreBoard = dict()
    for char in scoreTrack:
        if (char not in scoreBoard) and (char.islower() is True):
            scoreBoard[char] = 0
        if char.islower():
            scoreBoard[char] += 1
        if char.isupper():
            if char.lower() not in scoreBoard:
                scoreBoard[char.lower()] = 0
            scoreBoard[char.lower()] -= 1
    print(scoreBoard)


tally("EbAAdbBEaBaaBBdAccbeebaec")

