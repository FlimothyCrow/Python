

def mockCase(string):
    new_quote = ""
    i = False
    for char in string:
        if i:
            new_quote += char.upper()
        else:
            new_quote += char.lower()
        if char != ' ':
            i = not i
    return new_quote

print(mockCase("there's no such thing as reverse racism"))