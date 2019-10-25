import random

def randomNumber() :
    return random.randint(1,9)

#nouns = ["schmuck", "apple-john", "swine", "jerk", "Spaniard", "coconut", "goatherd"]

#modern = ["dickheaded", "illiterate", "vegan", "instagram", "pumpkin spice", "simple", "antivax"]

#shakespeare = ["goatish", "milk-livered", "poorly born", "tardy-gaited", "yeasty", "ill-nurtured"]

# we need to refer to each list and pull the element into a string (with enumerate maybe?)
# insultGenerator will take a string name and pull an element at random
# could we set it to choose from the lists in a random order?
# parsing data into a data structure is a huge part of the job
"""
def insultGenerator(set0, set1, set2) :
    finalInsult = (random.choice(set0))
    finalInsult = finalInsult + " " + (random.choice(set1))
    finalInsult = finalInsult + " " + (random.choice(set2))
    print(finalInsult)
"""
#insultGenerator(modern, shakespeare, nouns)

# split by string with newline
# split by comma
# assign each line to a variable
# contents gives us one long string

#print(contents)

def parseInsult(row, inputText):
    final = []
    rows = inputText.splitlines()
    singleRow = rows[row].split(",")
    for i in singleRow :
        final.append(i.strip())
    return final

def insultPuller(row0, row1, row2) :
    print((row0[randomNumber()]), row1[randomNumber()], row2[randomNumber()])

def insultGenerator(howMany):
    f = open("insults.txt", "r")
    contents = f.read()

    nouns = parseInsult(0, contents)
    modern = parseInsult(1, contents)
    shakespeare = parseInsult(2, contents)

    for i in range(howMany) :
        insultPuller(nouns, modern, shakespeare)

insultGenerator(10)