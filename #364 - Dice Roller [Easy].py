# https://old.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/

import re
import random


def rollDice(roll):
    matchObj = re.match(r'(\d*)d(\d*)', roll)
    noOfDice = matchObj.group(1)
    diceSize = matchObj.group(2)
    print(noOfDice, diceSize)
    diceSum = 0
    rolls = list()
    for i in range(int(noOfDice)):
        rollNum = random.randint(1, int(diceSize))
        diceSum += rollNum
        rolls.append(rollNum)
    print(diceSum, ":", rolls)

rollDice('6d4')