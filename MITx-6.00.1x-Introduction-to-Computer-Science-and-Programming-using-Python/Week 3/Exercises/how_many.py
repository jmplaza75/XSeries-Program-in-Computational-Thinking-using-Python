#!/usr/bin/env python3

def how_many(aDict):
	sum = 0
	for i in aDict.values():
		sum += len(i)
	return sum
