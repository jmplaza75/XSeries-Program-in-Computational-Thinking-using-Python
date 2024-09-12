#!/usr/bin/env python3

def getSublists(L, n):
	final_list = []
	z = len(L)-n+1
	for i in range(z):
		final_list.append(L[i:i+n])
	return final_list