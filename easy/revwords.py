#!/usr/bin/python

#https://www.codeeval.com/open_challenges/8/

import sys

f = open(sys.argv[1], 'r')

for string in f:
	words = string.split()
	print " ".join(words[::-1])
f.close()

