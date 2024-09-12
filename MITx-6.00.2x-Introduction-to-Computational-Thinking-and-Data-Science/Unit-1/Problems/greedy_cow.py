#!/usr/bin/env python3

def greedy_cow_transport(cows, limit=10):
	viajes = []
	cows_arra = sorted(cows.items(), key=lambda x: x[1], reverse=True)
	
	while sum(weight for _, weight in cows_arra) > 0:
		nave = []
		tot_val = 0
		for cow, weight in cows_arra:
			if weight != 0 and tot_val + weight <= limit:
				nave.append(cow)
				tot_val += weight
		# Mark transported cows
		cows_arra = [(cow, 0) if cow in nave else (cow, weight) for cow, weight in cows_arra]
		viajes.append(nave)
		
	return viajes



