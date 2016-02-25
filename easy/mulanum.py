#!/usr/bin/python

#https://www.codeeval.com/open_challenges/18/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		num = line.strip().split(',')
		x = int(num[0])
		n = m = int(num[1])
		while x > n:
			n += m
		print n

