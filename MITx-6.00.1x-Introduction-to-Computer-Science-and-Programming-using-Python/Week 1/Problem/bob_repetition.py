#!/usr/bin/env python3

count = 0
for j in range(len(s)-2):
	if s[j] == 'b' and s[j+1] == 'o' and s[j+2] == 'b':
		count = count + 1
print ("Number of times bob occurs is: " + str(count))