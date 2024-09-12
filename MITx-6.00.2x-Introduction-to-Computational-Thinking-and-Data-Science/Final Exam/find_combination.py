#!/usr/bin/env python3

import numpy as np
import itertools
def find_combination(choices, total):
	ps = []
	for p in itertools.product([1,0], repeat = len(choices)):
		ps.append(np.array(p))
	feq = []
	fl = []
	for z in ps:
		if sum(z*choices) == total:
			feq.append(z)
		elif sum(z*choices) < total:
			fl.append(z)
	if len(feq) > 0:
		res = min(enumerate(feq), key=lambda u:sum(u[1]))[1]
		return res
	else:
		res = max(enumerate(fl), key = lambda u:sum(u[1]))[1]
		return res