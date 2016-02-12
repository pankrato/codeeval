#!/usr/bin/python

"""Hex to Decimal
https://www.codeeval.com/open_challenges/67/"""

import sys

f = open(sys.argv[1], 'r')
for s in f:
	print int(s,16)

f.close()

