# https://old.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/


def checkUPC(UPC_Code):
    UPC_CodeList = list()
    for num in UPC_Code:
        UPC_CodeList.append(int(num))
    evenNumSum = 0
    oddNumSum = 0
    for numIndex, num in enumerate(UPC_CodeList):
        if numIndex % 2 is 0:
            evenNumSum += num
        else:
            oddNumSum += num
    evenNumSum = evenNumSum * 3
    finalSum = evenNumSum + oddNumSum
    finalSum = finalSum % 10
    if finalSum is not 0:
        finalSum = 10 - finalSum
    print(finalSum)


checkUPC("04210000526")