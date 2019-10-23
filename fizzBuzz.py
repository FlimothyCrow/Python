
def listRange(start, stop):
    return list(range(start, stop))


def wordChanger(numbers, target, replace):
    for (i, item) in enumerate(numbers) :
        if item % target == 0 :
            numbers[i] = replace
            return numbers




# line 10 is causing a print / return for each occurrence of target


# this program should take start, stop, target and replacer
# it will call listRange once and wordChanger twice
# then print the result

def listMutate(start, stop, target, replace):
    numbers = listRange(start, stop)
    print(wordChanger(numbers, target, replace))

#listMutate(1, 21, 3, "fizz")


mylist = [111, -222, 333, -444, -1, -2, -3]
for (i, item) in enumerate(mylist):
    if item < 0:
        mylist[i] = 0
#print(mylist)

