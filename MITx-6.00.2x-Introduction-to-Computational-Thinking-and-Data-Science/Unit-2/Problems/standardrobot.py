#!/usr/bin/env python3

class Robot(object):
	def __init__(self, room, speed):
		self.room = room
		self.speed = speed
		self.position = room.getRandomPosition()
		self.direction = random.randint(0, 359)
		self.room.cleanTileAtPosition(self.position)
		
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
		
class StandardRobot(Robot):
	def updatePositionAndClean(self):
		next_position = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.speed)
		if self.room.isPositionInRoom(next_position) == False:
			self.setRobotDirection(random.randint(0, 359))
		else:
			self.setRobotPosition(next_position)            
			self.room.cleanTileAtPosition(next_position)