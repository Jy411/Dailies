# https://www.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/
# WEIRD ERROR: ValueError: invalid literal for int() with base 10: ''
import math


def kaprekarNumbers(start, end):
    for i in range(start, end+1):
        num = int(math.pow(i, 2))
        numList = [int(num) for num in str(num)]
        print(i, numList, len(numList))
        secondHalfIndex = int(len(numList)/2)
        firstHalfVal = ""
        secondHalfVal = ""
        for val, digit in enumerate(numList):
            if val < secondHalfIndex:
                firstHalfVal += "".join(str(digit))
            if val >= secondHalfIndex:
                secondHalfVal += "".join(str(digit))
        print("first:", firstHalfVal, "second:", secondHalfVal)
        firstHalfVal = int(firstHalfVal)

        # finalVal = int(firstHalfVal.strip()) + int(secondHalfVal.strip())
        # print(finalVal)


kaprekarNumbers(1, 55)