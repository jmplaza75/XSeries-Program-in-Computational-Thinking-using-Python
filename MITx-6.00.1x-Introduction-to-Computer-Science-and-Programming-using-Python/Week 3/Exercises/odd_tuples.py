#!/usr/bin/env python3

def oddTuples(aTup):
	i = 0
	newTup = ()
	for index in aTup:
		if i%2 == 0:
			newTup += (index,)
		i += 1
	return newTup