# https://www.reddit.com/r/dailyprogrammer/comments/7i1ib1/20171206_challenge_343_intermediate_mozarts/

import random

musicComposition = open("mozart.txt")
measureList = list()
for line in musicComposition:
    line = line.replace("\n", "")
    measureList.append(line)
print(measureList)
groupOfMeasures = [measureList[i:i + 3] for i in range(0, len(measureList), 3)]
for group in groupOfMeasures:
    print(group)
choice = random.randint(0, len(measureList))
