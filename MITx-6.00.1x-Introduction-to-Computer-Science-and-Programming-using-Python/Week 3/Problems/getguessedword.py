#!/usr/bin/env python3

def getGuessedWord(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represents
		what letters in secretWord have been guessed so far.
	'''
	lett = ''
	for letter in secretWord:
		if letter in lettersGuessed:
			lett = lett + letter + ' '
		else:
			lett = lett + '_ '
	return lett


secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))