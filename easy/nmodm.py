#!/usr/bin/python

#https://www.codeeval.com/open_challenges/62/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		num = line.strip().split(',')
		n = int(num[0])
		m = int(num[1])
		while n >= m:
			n -= m
		print n

