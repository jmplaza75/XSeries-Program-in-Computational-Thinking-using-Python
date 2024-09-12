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
		if all([self.isResistantTo(i) for i in self.activeDrugs]) == True:
			probab = random.random()
			if probab <= self.maxBirthProb * (1 - self.popDensity):
				new_resistances = self.resistances.copy()
				for key in self.resistances.keys():
					probabi = random.random()
					if probabi <= self.getMutProb():
						if self.resistances[key] == True:
							new_resistances[key] = False
						else:
							new_resistances[key] = True
				return ResistantVirus(self.maxBirthProb, self.clearProb, new_resistances, self.mutProb)
			else:
				raise NoChildException
		else:
			raise NoChildException