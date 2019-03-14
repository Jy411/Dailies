# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

def gameOfThrees(number):
    while number != 1:
        if number % 3 == 0:
            print("%d 0" % number)
        elif number % 3 == 1:
            print("%d -1" % number)
            number -= 1
        elif number % 3 == 2:
            print("%d 1" % number)
            number += 1
        number = number / 3
    print(number)


userNum = int(input("Enter a number: "))
gameOfThrees(userNum)