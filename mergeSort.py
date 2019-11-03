def sortNumerical(numbers) :
    inOrder = sorted(numbers)
    return inOrder

# note that [0, 0, 0, 1] is "smaller" than [0, 0, 1]

def sortReverse(digits) :
    reverseOrder = sorted(digits, reverse=True)
    return reverseOrder

# [1, "a", 9, "x", 3, "b"], we've confirmed that sorted can't work with ints and letters together
# ["alphabet", "jerk store", "every time I die", "Curly's a dope"]
# capitals ARE taken into account, and are considered "smaller", they will list first

spicyList = [1, 31, 8, 29, 100, 5, 2, 9, 50]
dumbList = []


def mergeSort(numbers) :
    sortedList = []
    if len(numbers) > 1 :
        midPoint = len(numbers) // 2
        left = numbers[:midPoint]
        right = numbers[midPoint:]

        sortedLeft = mergeSort(left)
        sortedRight = mergeSort(right)

        while len(sortedLeft) > 0 or len(sortedRight) > 0: # if either has mass

            if len(sortedLeft) > 0 and not len(sortedRight) > 0: # if left has mass
                sortedList.append(sortedLeft[0])
                sortedLeft.pop(0)
            elif len(sortedRight) > 0 and not len(sortedLeft) > 0: # if right has mass
                sortedList.append(sortedRight[0])
                sortedRight.pop(0)
            elif sortedLeft[0] < sortedRight[0] : # both have mass
                sortedList.append(sortedLeft[0])
                sortedLeft.pop(0)
            else :
                sortedList.append(sortedRight[0])
                sortedRight.pop(0)
        return sortedList
    else :
        return numbers

print(mergeSort(spicyList))