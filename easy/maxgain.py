#!/usr/bin/python

#https://www.codeeval.com/open_challenges/186/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		words = line.strip().split(';')
		period = int(words[0])
		marks = [int(x) for x in words[1].split()]
		gain = [sum(marks[x:x+period:1]) for x in range(len(marks) - period + 1)]
		print max(gain) if max(gain) > 0 else 0

