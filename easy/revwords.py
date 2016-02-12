#!/usr/bin/python

#https://www.codeeval.com/open_challenges/20/

import sys

separator = " "

f = open(sys.argv[1], 'r')

for string in f:
	words = string.split( )
	revers = separator.join(words[::-1])
	print revers

f.close()

