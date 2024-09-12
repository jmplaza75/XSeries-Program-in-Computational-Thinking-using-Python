#!/usr/bin/env python3

class SimpleVirus(object):
	def __init__(self, maxBirthProb, clearProb):
		self.maxBirthProb = maxBirthProb
		self.clearProb = clearProb       
		
	def getMaxBirthProb(self):
		return self.maxBirthProb
	
	def getClearProb(self):
		return self.clearProb
	
	def doesClear(self):
		prob = random.random()
		if prob <= self.clearProb:
			return True
		else:
			return False
		
		
	def reproduce(self, popDensity):
		self.popDensity = popDensity
		proba = random.random()
		if proba <= self.maxBirthProb * (1 - self.popDensity):
			return SimpleVirus(self.maxBirthProb, self.clearProb)
		else:
			raise NoChildException
			
			
			
class Patient(object):
	def __init__(self, viruses, maxPop):
		self.viruses = viruses
		self.maxPop = maxPop
		
	def getViruses(self):
		return self.viruses
	
	
	def getMaxPop(self):
		return self.maxPop
	
	
	def getTotalPop(self):
		return len(self.viruses)
	
	
	def update(self):
		viruses_copy = self.viruses[:]
		for i in viruses_copy:
			if i.doesClear() == True:
				self.viruses.remove(i)
				
		popDensity = len(self.viruses)/self.maxPop
		
		viruses_copy_2 = self.viruses[:]
		for j in viruses_copy_2:
			try:
				j.reproduce(popDensity)
				self.viruses.append(j)
			except NoChildException:
				continue