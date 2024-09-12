#!/usr/bin/env python3

def lecture_activities(N, aLecture):
	l_day = []
	for trial in range(N):
		init_d = 1
		while (random.random() > aLecture.get_listen_prob()) or \
			(random.random() > aLecture.get_sleep_prob()) or \
			(random.random() > aLecture.get_fb_prob()) :
				init_d += 1
		l_day.append(init_d)
	(mean, std) = get_mean_and_std(l_day)
	return (round(mean, 3), round(1.96*std*2, 3))