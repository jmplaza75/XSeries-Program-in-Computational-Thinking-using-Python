#!/usr/bin/env python3

def gcdIter(a, b):
		'''
		a, b: positive integers
		
		returns: a positive integer, the greatest common divisor of a & b.
		'''
		if a <= b:
			smallest = a
		else:
			smallest = b
			
		for i in range(smallest,0,-1):
				if i == 1:
						return 1
				elif a % i == 0 and b % i == 0:
						return i
			