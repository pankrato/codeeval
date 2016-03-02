#!/usr/bin/python

#https://www.codeeval.com/open_challenges/91/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		numbers = line.strip().split(' ')
		floats = [float(x) for x in numbers]
		sort = [str('%.3f' % x) for x in sorted(floats)]
		print ' '.join(sort)
