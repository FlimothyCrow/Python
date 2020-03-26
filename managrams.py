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
# applicationsssssssssssss

def oddOrEven(inputNumber) :
    if not isinstance(inputNumber, int) :
        return "not an inputNumber"
    elif inputNumber == 0 :
        return "not applicable"
    elif inputNumber % 2 == 0 :
        return "even"
    else :
        return "odd"

#print(isinstance(0,int))

def spicyChange(inputCash) :
    hundreds = 0
    fifties  = 0
    twenties = 0
    while inputCash > 99 :
        inputCash -= 100
        hundreds += 1
        while inputCash > 49 :
            inputCash -= 50
            fifties += 1
            while inputCash > 19 :
                inputCash -= 20
                twenties += 1
    return fifties
