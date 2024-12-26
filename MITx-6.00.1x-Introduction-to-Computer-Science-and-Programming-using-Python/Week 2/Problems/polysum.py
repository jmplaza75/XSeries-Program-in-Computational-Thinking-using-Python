#!/usr/bin/env python3

import math as mm
def polysum(n,s):
	def area(n,s):
		area = (0.25 * n * s ** 2)/mm.tan(mm.pi/n)
		return area
	def Polyg(n,s):
		perimeter = n * s
		return perimeter
	sum = area(n,s) + (Polyg(n,s) ** 2)
	return round(sum,4)