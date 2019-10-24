def score(num) :
    if num == 0 :
        return "love"
    if num == 1 :
        return "fifteen"
    if num == 2 :
        return "thirty"
    if num == 3 :
        return "forty"

def tennis(p1, p2) :
    return score(p1) + " " + score(p2)

