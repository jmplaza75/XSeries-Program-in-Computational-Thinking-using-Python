#!/usr/bin/env python3

max = 0
c = s[0]
l = s[0]

for i in range(len(s) - 1): 
	if s[i+1] >= s[i]:
		c += s[i+1]
		if len(c) > max:
			max = len(c)
			l = c
	else:
		c = s[i+1]
	i += 1
print("The longest substring in alphabetical order is:" + l)