import random


def mockCase(string):
    new_quote = ""
    i = False
    for char in string:
        if i:
            new_quote += char.upper()
        else:
            new_quote += char.lower()
        if char != ' ':
            i = not i
    return new_quote


# print(mockCase("given two unsorted binary trees"))


def countNegatives(grid):
    negativeCounter = 0
    for arrayOfNums in grid:
        for num in arrayOfNums:
            if num < 0:
                negativeCounter += 1
    return negativeCounter

def selfDividing(num):
    for char in str(num):
        if num % int(char) != 0:
            return False
    return True

def countEvenLengths(nums):
    countOfEvens = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            countOfEvens += 1
    return countOfEvens

def squareIsWhite(coordinates):
    blackStart = ["a", "c", "e", "g"]
    if coordinates[0] in blackStart:
        if int(coordinates[1]) % 2 == 0:
            return True
        else:
            return False
    else:
        if int(coordinates[1]) % 2 == 0:
            return False
        else :
            return True