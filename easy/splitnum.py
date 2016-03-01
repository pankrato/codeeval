#!/usr/bin/python

#https://www.codeeval.com/open_challenges/131/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		words = line.strip().split(' ')
		number = words[0].strip()
		pattern = words[1].strip()
		if '+' in pattern:
			index = pattern.index('+')
			a = int(number[0:index])
			b = int(number[index::])
			print a+b
		elif '-' in pattern:
			index = pattern.index('-')
			a = int(number[0:index])
			b = int(number[index::])
			print a-b

