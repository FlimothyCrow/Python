import random

def randomNumber() :
    return random.randint(1,10)

nouns = ["schmuck", "apple-john", "swine", "jerk", "Spaniard", "coconut", "goatherd"]

modern = ["dickheaded", "illiterate", "vegan", "instagram", "pumpkin spice", "simple", "antivax"]

shakespeare = ["goatish", "milk-livered", "poorly born", "tardy-gaited", "yeasty", "ill-nurtured"]

# we need to refer to each list and pull the element into a string (with enumerate maybe?)
# insultGenerator will take a string name and pull an element at random
# could we set it to choose from the lists in a random order?

def insultGenerator(set0, set1, set2) :
    finalInsult = (random.choice(set0))
    finalInsult = finalInsult + " " + (random.choice(set1))
    finalInsult = finalInsult + " " + (random.choice(set2))
    print(finalInsult)

insultGenerator(modern, shakespeare, nouns)