#!/usr/bin/env python3

def uniqueValues(aDict):
	'''
	aDict: a dictionary
	returns: a sorted list of keys that map to unique aDict values, empty list if none
	'''
	Var_tmp = {}
	list_of_keys = []
	for value in aDict.values():
		if(value in Var_tmp.keys()): Var_tmp[value] += 1
		else: Var_tmp[value] = 1
	for key in aDict.keys():
		if(Var_tmp[aDict[key]] == 1): list_of_keys.append(key)
	return sorted(list_of_keys)