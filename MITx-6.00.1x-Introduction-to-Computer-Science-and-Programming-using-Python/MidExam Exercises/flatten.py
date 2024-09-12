#!/usr/bin/env python3

def flatten(aList):
	newList = []
	for item in aList:
		if type(item) != type([]):
			newList.append(item)
		else:
			newList.extend(flatten(item))
	return newList