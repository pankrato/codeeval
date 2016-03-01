#!/usr/bin/python

#https://www.codeeval.com/open_challenges/112/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		words = line.strip().split(':')
		numbers = words[0].strip().split()
		positions = words[1].strip().split(',')
		for pos in positions:
			pair = pos.strip().split('-')
			left = int(pair[0])
			right = int(pair[1])
			numbers[left], numbers[right] = numbers[right], numbers[left]
		print ' '.join(numbers)

