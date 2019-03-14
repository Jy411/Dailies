# https://www.reddit.com/r/dailyprogrammer/comments/wvc21/7182012_challenge_79_easy_counting_in_steps/

import math

def step_count(a, b, step):
    difference = b - a
    count = difference/(step-1)
    numList = []
    for i in range(step):
        numList.append(a + (i*count))
    print(numList)


print(step_count(13.50, -20.75, 3))