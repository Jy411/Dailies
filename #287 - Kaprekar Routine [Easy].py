# https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/


def largestDigit(digit):
    numbers = list(map(int, str(digit)))
    return max(numbers)


def descendingOrder(digit):
    numbers = list(map(int, str(digit)))
    numbers.sort(reverse=True)
    s = [str(i) for i in numbers]
    result = int("".join(s))
    return result


def ascendingOrder(digit):
    numbers = list(map(int, str(digit)))
    numbers.sort()
    s = [str(i) for i in numbers]
    result = int("".join(s))
    return result


def kaprekarRoutine(descNum, ascNum):
    num = 0
    i = 0
    while num != 6174:
        num = int(descNum) - int(ascNum)
        ascNum = ascendingOrder(num)
        descNum = descendingOrder(num)
        print(num)
        i += 1
    print(i)


desc = descendingOrder(5455)
asc = ascendingOrder(5455)
kaprekarRoutine(desc, asc)