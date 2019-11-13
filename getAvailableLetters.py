import string
alph = string.ascii_lowercase
def getAvailableLetters(lettersGuessed):
    remain = []
    for y in alph:
        if y not in lettersGuessed:
            remain.append(y)
    return ''.join(remain)