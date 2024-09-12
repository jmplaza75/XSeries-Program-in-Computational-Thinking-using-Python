#!/usr/bin/env python3

import string

def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
		yet been guessed.
	'''
	import string
	lettersNotGuessed = string.ascii_lowercase
	for letter in lettersGuessed:
		if letter in lettersNotGuessed:
			lettersNotGuessed = lettersNotGuessed.replace(letter,'')
	return lettersNotGuessed

print(string.ascii_lowercase)