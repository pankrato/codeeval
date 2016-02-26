#!/usr/bin/python

#https://www.codeeval.com/open_challenges/92/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		num = line.strip().split()
		print num[-2]

