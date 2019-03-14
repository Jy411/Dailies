# https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/20151130_challenge_243_easy_abundant_and/

def numType(number):
    divisors = list()
    sumOfDivisors = 0
    for x in range(1, number+1):
        if number % x == 0:
            divisors.append(x)
    for num in divisors:
        sumOfDivisors += num
    if sumOfDivisors < 2*number:
        print(number, "is deficient by", sumOfDivisors-2*number)
    elif sumOfDivisors > 2*number:
        print(number, "is abundant by", sumOfDivisors-2*number)
    else:
        print(number, "neither deficient or abundant")


test = [111, 112, 220, 69, 134, 85]
for num in test:
    numType(num)
