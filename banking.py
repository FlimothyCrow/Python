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

def entryValidator(d) :
    if len(d) == 9 :
        if (abs(d[8]) + 2 * abs(d[7]) + 3 * abs(d[6]) + 4 *
            abs(d[5]) + 5 * abs(d[4]) + 6 * abs(d[3]) + 7 *
            abs(d[2]) + 8 * abs(d[1]) + 9 * abs(d[0])) % 11 == 0 :
            return True








#print("012345678"[0])






# 0 = 0-4
# 1 = 4-8
# 2 = 8-12

# one function as a list (int)
# another for single digits
