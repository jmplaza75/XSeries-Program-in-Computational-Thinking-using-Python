#!/usr/bin/env python3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
					robot_type):
	results = []
	for i in range(num_trials):
		num_steps = 0
		room = RectangularRoom(width, height)
		robots = [robot_type(room, speed) for j in range(num_robots)]
		while (room.getNumCleanedTiles()/room.getNumTiles()) < min_coverage:
			num_steps += 1
			for k in robots:
				k.updatePositionAndClean()
			if (room.getNumCleanedTiles()/room.getNumTiles()) >= min_coverage:
				results.append(num_steps)
			else:
				continue
	return sum(results)/len(results)
