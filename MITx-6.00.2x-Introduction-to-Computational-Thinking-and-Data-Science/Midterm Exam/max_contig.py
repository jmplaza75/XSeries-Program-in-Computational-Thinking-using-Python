#!/usr/bin/env python3

def max_contig_sum(L):
	""" L, a list of integers, at least one positive
		Returns the maximum sum of a contiguous subsequence in L """
	temp = 0
	fin = 0
	for s in L:
		fin = max(fin + s, 0)
		temp = max(temp, fin)
	return temp