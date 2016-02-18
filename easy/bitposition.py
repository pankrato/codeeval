#!/usr/bin/python

#https://www.codeeval.com/open_challenges/19/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		numbers = line.split(',')
		i = int(numbers[0])
		p1 = int(numbers[1])-1
		p2 = int(numbers[2])-1
		if ((i>>p1) & 1) ^ ((i>>p2) & 1):
			print 'false'
		else:
			print 'true'

