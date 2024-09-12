#!/usr/bin/env python3

import numpy as np

def generate_models(x, y, degs):
	fit_model = []
	for i in degs:
		fit_model = fit_model + [np.polyfit(x,y,i)]   
	return fit_model
