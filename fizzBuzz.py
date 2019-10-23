
def listRange(start, stop):
    return list(range(start, stop))


def wordChanger(numbers, target, replace):
    for (i, item) in enumerate(numbers) :
        if item % target == 0 :
            numbers[i] = replace
    return numbers



def listMutate(numbers, target1, replace1):
    mutation = wordChanger(numbers, target1, replace1)


listMutate([1, 2, 3, 4, 5, 6, 7, 8], 3, "jerk")

#def multipleMutate(start, stop) :
