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


def returnEven(arr):
    return list(filter(lambda x: x % 2 == 0, arr))

def runningSum(nums):
    arrayOfSums = []
    runningSum = 0
    for index in range(len(nums)):
        runningSum += nums[index]
        arrayOfSums.append(runningSum)
    return arrayOfSums

def defangingIP(address):
    addressCopy = list(address)
    for index in range(len(address)):
        if address[index] == ".":
            addressCopy[index] = "[.]"
    return "".join(addressCopy)

# print(mockCase("stab them with an icicle, it'll melt and they won't find your fingerprints"))



