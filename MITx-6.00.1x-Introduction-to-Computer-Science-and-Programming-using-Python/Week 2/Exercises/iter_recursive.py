#!/usr/bin/env python3

def recurPower(base, exp):
	'''
	base: int or float.
	exp: int >= 0

	returns: int or float, base^exp
	'''
def recurPower(base,exp):
	if exp == 0:
		return base * exp+1
	else:
		return base * recurPower(base, exp-1)