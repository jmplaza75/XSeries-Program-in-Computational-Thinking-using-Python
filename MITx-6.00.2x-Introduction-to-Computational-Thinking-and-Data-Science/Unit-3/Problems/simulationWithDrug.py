#!/usr/bin/env python3

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
						mutProb, numTrials):
	import numpy as np
	
	dat = np.zeros(300)
	dat_1 = np.zeros(300)
	for p in range(numTrials):
		vir = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
		vir_2 = [vir] * numViruses
		pat = TreatedPatient(vir_2, maxPop)
		count, resist_virus_count = [], []
		for u in range(150):
			pat.update()
			count.append(pat.getTotalPop())
			resist_virus_count.append(pat.getResistPop(['guttagonol']))
		pat.addPrescription('guttagonol')
		for r in range(150):
			pat.update()
			count.append(pat.getTotalPop())
			resist_virus_count.append(pat.getResistPop(['guttagonol']))
		dat = dat + count
		dat_1 = dat_1 + resist_virus_count
	med = dat/numTrials
	med_2 = dat_1/numTrials
	
	pylab.plot(list([float('{0:.1f}'.format(i)) for i in med]), label = 'Non-resistant population')
	pylab.plot(list([float('{0:.1f}'.format(j)) for j in med_2]), label = 'Guttagonol Resistant population')
	pylab.xlabel('steps')
	pylab.ylabel('Average Population')
	pylab.title('Simulation')
	pylab.legend()
	pylab.show()