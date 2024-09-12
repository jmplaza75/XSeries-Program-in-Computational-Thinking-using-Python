#!/usr/bin/env python3

def calculateHandlen(hand):
	""" 
	Returns the length (number of letters) in the current hand.
	
	hand: dictionary (string int)
	returns: integer
	"""
	suma = 0
	for value in hand.values():
		suma += value
	return suma