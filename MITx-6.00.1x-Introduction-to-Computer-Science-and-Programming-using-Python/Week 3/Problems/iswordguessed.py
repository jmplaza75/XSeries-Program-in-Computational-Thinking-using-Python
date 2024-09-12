#!/usr/bin/env python3

def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secretWord are in lettersGuessed;
		False otherwise
	'''
	fin = True
	for letter in secretWord:
		if letter in lettersGuessed:
			fin = True
		else:
			return not fin
	return fin

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))