#!/usr/bin/python

#https://www.codeeval.com/open_challenges/31/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		words = line.split(',')
		print words[0].rfind(words[1].rstrip('\n'))

