def isWordGuessed(secretWord, lettersGuessed):
    t = 0
    for s, letter in enumerate(secretWord):
    	if letter in lettersGuessed:
    		t += 1
    if t == len(secretWord):
    	return True
    else:
    	return False
