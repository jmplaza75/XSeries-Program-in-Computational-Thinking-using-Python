#!/usr/bin/env python3

import random
def stochasticNumber():
	'''
	Stochastically generates and returns a uniformly distributed even number between 9 and 21
	'''
	return random.randrange(10, 21, 2)