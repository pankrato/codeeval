#!/usr/bin/python

#https://www.codeeval.com/open_challenges/237/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		inp = line.strip().split('|')
		virus = [int(x, base=16) for x in (inp[0].strip().split())]
		antivirus = [int(x, base=2) for x in (inp[1].strip().split())]
		print sum(antivirus) >= sum(virus)
