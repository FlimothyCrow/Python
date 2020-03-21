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
        if element % 3 == 0 and element % 4 == 0 :
            parsedList.append("fizz buzz")
        elif element % 4 == 0 :
            parsedList.append("buzz")
        elif element % 3 == 0 :
            parsedList.append("fizz")
        else :
            parsedList.append(element)
    return parsedList
# anagram compatibility generator assessment
# applications