def listRange(start, stop):
    return list(range(start, stop))


def wordNums(numbers, replace):
    for (i, item) in enumerate(numbers) :
        if item % 3 == 0 :
            numbers[i] = replace
            return numbers

wordNums([1,2,3,4], "Jerk")

