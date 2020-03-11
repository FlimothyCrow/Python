"""
def score(num) :
    if num == 0 :
        return "love"
    if num == 1 :
        return "fifteen"
    if num == 2 :
        return "thirty"
    if num == 3 :
        return "forty"
"""


def whoWins(p1, p2) :
    if p1 > p2 :
        return "player 1"
    else : return "player 2"


def returnLargest(listOfInputs) :
    orderedList = sorted(listOfInputs, key=None, reverse=False)
    return orderedList[-1]


def removeDupes(mixedList) :
    flattened = {}
    singles = {}
    dupes = {}
    for element in mixedList :
        if element in flattened :
            flattened[element] += 1
        else :
            flattened[element] = 1

    for key, value in flattened.items() :
        if value == 1 :
            singles[key] = 1
        else :
            dupes[key] = 2
    return dupes

