one = ["   ",
       "  |",
       "  |",
       "   "]

two = [" _ ",
       " _|",
       "|_ ",
       "   "]

three = [" _ ",
         " _|",
         " _|",
         "   "]

four = ["   ",
        "|_|",
        "  |",
        "   "]

five = [" _ ",
        "|_ ",
        " _|",
        "   "]

six =  [" _ ",
        "|_ ",
        "|_|",
        "   "]

seven = [" _ ",
         "  |",
         "  |",
         "   "]

eight = [" _ ",
         "|_|",
         "|_|",
         "   "]

nine = [" _ ",
        "|_|",
        " _|",
        "   "]

zero = [" _ ",
        "| |",
        "|_|",
        "   "]

def parseEntries(entry, digit, txt) :
    final = []
    rows = txt.splitlines() # a list that's 4 long
    startRow = entry * 4
    for rowIndex in range(startRow, startRow + 4) :
        start = digit * 3
        end = start + 3
        final.append(rows[rowIndex][start:end])
    if final == one :
        return 1
    elif final == two :
        return 2
    elif final == three :
        return 3
    elif final == four:
        return 4
    elif final == five:
        return 5
    elif final == six:
        return 6
    elif final == seven:
        return 7
    elif final == eight:
        return 8
    elif final == nine:
        return 9
    elif final == zero:
        return 0


def textReader() :
    f = open("bankInput.txt", "r")
    contents = f.read()
    return contents

def entryValidator(account) :
    if len(account) == 9 :
        if abs(account[0]) + abs(account[1]) == 3 :
            return True

            #(d1+2*d2+3*d3+4*d4+5*d5+6*d6+7*d7+8*d8+9*d9) mod 11 = 0




#print("012345678"[0])






# 0 = 0-4
# 1 = 4-8
# 2 = 8-12

# one function as a list (int)
# another for single digits
