#!/usr/bin/env python3

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials):
	import numpy as np
	
	dat = np.zeros(300)
	for iter in range(numTrials):
		vir_1 = SimpleVirus(maxBirthProb, clearProb)
		vir_2 = [vir_1] * numViruses
		pat = Patient(vir_2, maxPop)
		count = []
		for iter_2 in range(300):
			pat.update()
			count.append(pat.getTotalPop())            
		dat = dat + count
	med = dat/numTrials
	
	pylab.plot(list(med), label=r'SimpleVirus')
	pylab.title("SimpleVirus simulation")
	pylab.xlabel("Time Steps")
	pylab.ylabel("Average Virus Population")
	pylab.legend(loc = "best")
	pylab.show()