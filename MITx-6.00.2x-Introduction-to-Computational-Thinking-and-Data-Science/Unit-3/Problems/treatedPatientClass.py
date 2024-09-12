#!/usr/bin/env python3

class ResistantVirus(SimpleVirus):
	
	def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
		super().__init__(maxBirthProb, clearProb)
		self.resistances = resistances
		self.mutProb = mutProb
		
		
	def getResistances(self):
		return self.resistances
	
	def getMutProb(self):
		return self.mutProb
	
	def isResistantTo(self, drug):
		try:
			return self.resistances[drug]
		except KeyError:
			return False
		
		
	def reproduce(self, popDensity, activeDrugs):
		self.popDensity = popDensity
		self.activeDrugs = activeDrugs
		if all([self.isResistantTo(p) for p in self.activeDrugs]) == True:
			prob_1 = random.random()
			if prob_1 <= self.maxBirthProb * (1 - self.popDensity):
				res = self.resistances.copy()
				for key in self.resistances.keys():
					prob_2 = random.random()
					if prob_2 <= self.getMutProb():
						if self.resistances[key] == True:
							res[key] = False
						else:
							new_resistances[key] = True
				return ResistantVirus(self.maxBirthProb, self.clearProb, res, self.mutProb)
			else:
				raise NoChildException
		else:
			raise NoChildException
			
			
class TreatedPatient(Patient):
	def __init__(self, viruses, maxPop):
		super().__init__(viruses, maxPop)
		self.prescription = []
		
		
	def addPrescription(self, newDrug):
		self.newDrug = newDrug
		if self.newDrug not in self.prescription:
			self.prescription.append(self.newDrug)
			
			
	def getPrescriptions(self):
		return self.prescription
	
	
	def getResistPop(self, drugResist):
		self.drugResist = drugResist
		resist_pop = 0
		for i in self.viruses:
			if all([i.isResistantTo(j) for j in self.drugResist]) == True:
				resist_pop += 1
		return resist_pop
	
	
	def update(self):
		vir_1 = self.viruses[:]
		for iter_1 in vir_1:
			if iter_1.doesClear() == True:
				self.viruses.remove(iter_1)         
		popDensity = len(self.viruses)/self.maxPop
		
		vir_2 = self.viruses[:]
		for iter_2 in vir_2:
			try:
				iter_2.reproduce(popDensity, self.prescription)
				self.viruses.append(iter_2)
			except NoChildException:
				continue