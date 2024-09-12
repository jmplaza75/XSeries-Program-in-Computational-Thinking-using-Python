#!/usr/bin/env python3

def iterPower(base, exp):
	'''
	base: int or float.
	exp: int >= 0

	returns: int or float, base^exp
	'''
	# Your code here
	a = 1
	while exp > 0:
		a = (a * base)
		exp -= 1
	return a