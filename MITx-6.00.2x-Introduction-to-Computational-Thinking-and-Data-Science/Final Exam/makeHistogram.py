#!/usr/bin/env python3

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
		"""
			- values, a list of numbers
			- numBins, a positive int
			- xLabel, yLabel, title, are strings
			- Produces a histogram of values with numBins bins and the indicated labels
				for the x and y axes
			- If title is provided by caller, puts that title on the figure and otherwise
				does not title the figure
		"""
		pylab.hist(values, bins = numBins)
		pylab.xlabel(xLabel)
		pylab.ylabel(yLabel)
		if title != None:
				pylab.title(title)
		pylab.show()