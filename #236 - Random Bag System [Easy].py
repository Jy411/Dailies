# https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/
import random

def tetrisPieces():
    pieces = ["O", "I", "S", "Z", "L", "J", "T"]
    random.shuffle(pieces)
    finalOutput = ""
    while len(finalOutput) < 50:
        finalOutput += random.choice(pieces)
    print(finalOutput)
    return finalOutput

# not fully working as intended
def verify(inp):
    for i in range(1, 8):
        print(i)
        chunk = inp[(7*(i-1)):(i*7)]
        pieces = ""
        print(chunk)
        for c in chunk:
            if c in pieces:
                print('repeat')
            else:
                pieces += c


verify(tetrisPieces())