#!/usr/bin/python

#https://www.codeeval.com/open_challenges/82/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		number = line.strip()
		power = len(number)
		result = 0
		for digit in range(power):
			result += pow(int(number[digit]),power)
		print 'True' if result == int(number) else 'False'

