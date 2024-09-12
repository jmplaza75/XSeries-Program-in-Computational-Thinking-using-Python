#!/usr/bin/env python3

def general_poly (L):    
	def func(x):
		valor = 0
		long = len(L) - 1
		for count in L:
			valor = valor + count * (x ** long)
			long -= 1
		return valor
	return func