
def listRange(start, stop):
    return list(range(start, stop))


def wordChanger(numbers, target, replace):
    for (i, item) in enumerate(numbers) :
        if item % target == 0 :
            numbers[i] = replace
    return numbers



def listMutate(start, stop, target, replace):
    numbers = listRange(start, stop)
    print(wordChanger(numbers, target, replace))

#listMutate(1, 21, 3, "fizz")


