#!/usr/bin/env python3

def brute_force_cow_transport(cows, limit=10):
	best_solution = None
	
	for partition in get_partitions(cows):
		valid_partition = True
		
		for trip in partition:
			trip_weight = sum(cows[cow] for cow in trip)
			
			if trip_weight > limit:
				valid_partition = False
				break
			
		if valid_partition:
			if best_solution is None or len(partition) < len(best_solution):
				best_solution = partition
				
	return best_solution

