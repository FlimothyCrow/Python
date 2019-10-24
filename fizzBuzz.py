def listRange(start, stop):
    return list(range(start, stop))


def wordChanger(numbers, target, replace):
    newList = []
    for num in numbers :
        if isinstance(num, int) :
            if num % target == 0 :
                newList.append(replace)
            else :
                newList.append(num)
        else :
            newList.append(num)
    return newList



def listMutate(numbers, target1, replace1, target2, replace2):
    mutation = wordChanger(numbers, target1, replace1)
    return wordChanger(mutation, target2, replace2)



#print(listMutate([1, 2, 3, 4, 5, 6, 7, 8], 3, "jerk", 2, "schmo"))



