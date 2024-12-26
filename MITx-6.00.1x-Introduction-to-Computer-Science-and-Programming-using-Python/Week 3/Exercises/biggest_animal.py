#!/usr/bin/env python3

def biggest(aDict):
	fin = None
	biggestValue = 0
	for key in aDict.keys():
		if len(aDict[key]) >= biggestValue:
			fin = key
			biggestValue = len(aDict[key])
	return fin