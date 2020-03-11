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


class UserMainCode(object):
    @classmethod
    def max(cls, input1, input2, input3):
        nestedList = []
        for row in range(input1) :
            innerList = []
            for column in range(input2):
                #print(row, column)
                innerList.append(input3.pop(0))
            nestedList.append(innerList)
        return nestedList
        pass

def anagrams(list0, list1) :
    orderedList0 = sorted(list0, key = str)
    orderedList1 = sorted(list1, key = str)
    if orderedList0 == orderedList1 :
        return True
    else:
        return False
