#!/usr/bin/python

#https://www.codeeval.com/open_challenges/24/

import sys

with open(sys.argv[1], 'r') as f:
	print sum([int(x) for x in f])

