# https://old.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/


def findFactors(number):
    factorList = list()
    sumList = list()
    for i in range(1, number + 1):
        if number % i is 0:
            factorList.append(i)
    for num in factorList:
        for num2 in factorList:
            result = num * num2
            if result == number:
                sumOfFactors = num + num2
                if sumOfFactors not in sumList:
                    sumList.append(sumOfFactors)
    print(number, "=>", min(sumList))


findFactors(4444445)