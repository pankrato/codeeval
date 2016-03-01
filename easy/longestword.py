#!/usr/bin/python

#https://www.codeeval.com/open_challenges/111/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		words = line.strip().split()
		lenght = [len(x) for x in words]
		print words[lenght.index(max(lenght))]




