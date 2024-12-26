#!/usr/bin/env python3

def yieldAllCombos(items):
	N = len(items)
	# enumerate the 3**N possible combinations
	for i in range(3**N):
		bag_1 = []
		bag_2 = []
		for j in range(N):
			z = 3**j
			if (i // z) % 3 == 0:
				bag_1.append(items[j])
			elif (i // z) % 3 == 1:
				bag_2.append(items[j])
		yield (bag_1, bag_2)