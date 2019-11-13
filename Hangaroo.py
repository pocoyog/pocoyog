import string
alph = string.ascii_lowercase
print ("Hey! Welcome to Hangaroo Let's start by choosing any word. Type it like: The game hangaroo('word')")
def isWordGuessed(secretWord, lettersGuessed):
    t = 0
    for s, letter in enumerate(secretWord):
    	if letter in lettersGuessed:
    		t += 1
    if t == len(secretWord):
    	return True
    else:
    	return False
def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for l in secretWord:
        if l in lettersGuessed:
            result.append(l)
        else:
            result.append('_')
    return ' '.join(result)
def getAvailableLetters(lettersGuessed):
    remain = []
    for y in alph:
        if y not in lettersGuessed:
            remain.append(y)
    return ''.join(remain)
def hangaroo(secretWord):
    print('Hey Hey we are about to start!')
    print('If I have a word I think it would be..', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 5 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('-------')
            print('Nice Champ!')
            break
        else:
        	print('--------')
        	print('Your remaining', 5 - mistakesMade, 'chances left, you got this!')
        	print('Letters that maybe you forgotten:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Hit me up with a letter:  ')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Sweeeeet: ', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Bruh quit playin! you already chose that", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Bruh quit playin! this is not valid", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 5 - mistakesMade == 0:
        	print('-------')
        	print('Take this L', secretWord)
        	break
        else:
        	continue