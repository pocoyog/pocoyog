def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for l in secretWord:
        if l in lettersGuessed:
            result.append(l)
        else:
            result.append('_')
    return ' '.join(result)