#!/usr/bin/env python3

def isIn(char, aStr):
		'''
		char: a single character
		aStr: an alphabetized string
		
		returns: True if char is in aStr; False otherwise
		'''
		if len(aStr)==1 and aStr[0] != char:
			return False
		if aStr=='':
			return False
	
		med = int((0+ len(aStr))/2)
	
		if aStr[med] == char:
			return True
		else:
			if aStr[med] < char:
				return isIn(char, aStr[med+1:])
			elif aStr[med] > char:
				return isIn(char, aStr[0:med])