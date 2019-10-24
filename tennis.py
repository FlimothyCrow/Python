def score(num) :
    if num == 0 :
        return "love"
    if num == 1 :
        return "fifteen"
    if num == 2 :
        return "thirty"
    if num == 3 :
        return "forty"

def victory(p1, p2) :
   if max(p1, p2) - min(p1, p2) > 1 :
       if max(p1, p2) > 3 :
           return True

def whoWins(p1, p2) :
    if p1 > p2 :
        return "player 1"
    else : return "player 2"


def tennis(p1, p2) :
    if victory(p1, p2) :
        print("victory", whoWins(p1, p2))
    elif p1 and p2 > 2 :
        if p1 == p2 :
            return "deuce"
    else :
        return score(p1) + " " + score(p2)

tennis(4,3)

