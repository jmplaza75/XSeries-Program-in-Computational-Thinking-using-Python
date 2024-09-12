#!/usr/bin/env python3

class RectangularRoom(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.cleaned_tiles = []
		
	def cleanTileAtPosition(self, pos):
		point = (int(pos.getX()), int(pos.getY()))
		if point not in self.cleaned_tiles:
			self.cleaned_tiles.append(point)
			
	def isTileCleaned(self, m, n):
		self.m = m
		self.n = n
		tile = (self.m, self.n)
		if tile in self.cleaned_tiles:
			return True
		else:
			return False
		
	def getNumTiles(self):
		return self.width * self.height
	
	def getNumCleanedTiles(self):
		return len(self.cleaned_tiles)
	
	def getRandomPosition(self):
		randx = random.uniform(0, self.width)
		randy = random.uniform(0, self.height)
		return Position(randx, randy)
	
	
	def isPositionInRoom(self, pos):
		if pos.x >= 0 and pos.x < self.width and pos.y >= 0 and pos.y < self.height:
			return True
		else:
			return False