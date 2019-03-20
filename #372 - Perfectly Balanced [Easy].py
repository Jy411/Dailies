# https://old.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/


def isBalanced(userInput):
    userInput = list(userInput)
    x = 0
    y = 0
    for char in userInput:
        if char is 'x':
            x += 1
        if char is 'y':
            y += 1
    if x is y:
        return True
    else:
        return False


print(isBalanced("yyxyxxyxxyyyyxxxyxyx"))