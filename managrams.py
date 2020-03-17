def anagrams(list0, list1) :
    orderedList0 = sorted(list0, key = str)
    orderedList1 = sorted(list1, key = str)
    if orderedList0 == orderedList1 :
        return True
    else:
        return False


def fizzBuzz(listOfInts) :
    parsedList = []
    for element in listOfInts :
        if element % 3 == 0 :
            parsedList.append("fizz")
        elif element % 4 == 0 :
            parsedList.append("buzz")
        else :
            parsedList.append(element)
    return parsedList

def ifAnd(listToParse) :
    if listToParse[0] == 1 and listToParse[1] == 2 :
        return True
    elif listToParse[2] % 5 == 0 :
        return False # this won't trip if the first one has already tripped!
