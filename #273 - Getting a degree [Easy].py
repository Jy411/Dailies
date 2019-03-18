# https://www.reddit.com/r/dailyprogrammer/comments/4q35ip/20160627_challenge_273_easy_getting_a_degree/

import math
import re


def conversionParser(inputString):
    values = re.findall("\d+.\d+|\d+", inputString)
    units = re.findall("[a-z][a-z]", inputString)
    firstUnit = units[0][0]
    secondUnit = units[0][1]
    value = values[0]
    if value.find("."):
        return firstUnit, secondUnit, float(value)
    else:
        return firstUnit, secondUnit, int(value)


def converter(unit1, unit2, val):
    if unit1 is 'd':
        radianVal = math.radians(val)
        return str(radianVal) + " radians"
    elif unit1 is 'r':
        degreeVal = math.degrees(val)
        return str(degreeVal) + " degrees"
    elif unit1 is 'c':
        if unit2 is 'f':
            fahrenheitVal = (val * 9/5) + 32
            return str(fahrenheitVal) + " fahrenheits"
        if unit2 is 'k':
            kelvinVal = val + 273.15
            return str(kelvinVal) + " kelvins"
        else:
            return "Invalid conversion units"
    elif unit1 is 'f':
        if unit2 is 'c':
            celsiusVal = (val - 32) * 5/9
            return str(celsiusVal) + " celsius"
        if unit2 is 'k':
            kelvinVal = (val - 32) * 5/9 + 273.15
            return str(kelvinVal) + " kelvins"
        else:
            return "Invalid conversion units"
    elif unit1 is 'k':
        if unit2 is 'c':
            celsiusVal = (val - 273.15)
            return str(celsiusVal) + " celsius"
        if unit2 is 'f':
            fahrenheitVal = (val - 273.15) * 9/5 + 32
            return str(fahrenheitVal) + " fahrenheits"
        else:
            return "Invalid conversion units"


conUnit1, conUnit2, currVal = conversionParser("90dr")
print(converter(conUnit1, conUnit2, currVal))