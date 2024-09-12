#!/usr/bin/env python3

import numpy as np

def r_squared(y, estimated):
	y =  np.array(y)
	estimated = np.array(estimated)
	numerador = sum((estimated - y)**2)
	media_y = np.mean(y)
	denominador = sum((np.mean(y) - y)**2)
	return 1 - numerador / denominador