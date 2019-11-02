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

