#!/usr/bin/env python3

def getAverage(die, numRolls, numTrials):
	runs = []
	for p in range(numTrials):
		rolls = [die.roll() for q in range(numRolls)]
		tam = 1
		max_tam = 0
		for z in range(len(rolls)-1):
			if rolls[z+1] == rolls[z]:
				tam += 1
			else: 
				tam = 1
			if max_tam < tam:
				max_tam = tam
		if max_tam > 0:
			runs.append(max_tam)
		else:
			runs.append(1)
	makeHistogram(runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
	return sum(runs)/len(runs)