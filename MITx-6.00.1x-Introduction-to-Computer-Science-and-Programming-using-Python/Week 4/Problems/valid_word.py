#!/usr/bin/env python3

def isValidWord(word, hand, wordList):
	"""
	Returns True if word is in the wordList and is entirely
	composed of letters in the hand. Otherwise, returns False.

	Does not mutate hand or wordList.
	
	word: string
	hand: dictionary (string -> int)
	wordList: list of lowercase strings
	"""
	hd=hand.copy()
	for char in word:
		if char not in hd or hd[char]<=0:
			return False
		else:
			hd[char] -=1
	if word in wordList:
		return True
	return False