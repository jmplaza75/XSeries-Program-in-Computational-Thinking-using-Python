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
		
		
		
class Robot(object):
	def __init__(self, room, speed):
		self.room = room
		self.speed = speed
		self.position = room.getRandomPosition()
		self.direction = random.randint(0, 359)
		
	def getRobotPosition(self):
		return self.position
	
	def getRobotDirection(self):
		return self.direction
	
	def setRobotPosition(self, position):
		self.position = position
		
	def setRobotDirection(self, direction):
		self.direction = direction
		
	def updatePositionAndClean(self):
		raise NotImplementedError