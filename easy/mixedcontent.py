#!/usr/bin/python

#https://www.codeeval.com/open_challenges/115/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		string = line.split(',')
		numbers, words = [], []
		for element in range(len(string)):
			if string[element].strip().isdigit():
				numbers.append(string[element].strip())
			else:
				words.append(string[element].strip())
		if words and numbers:
			print ",".join(words) + '|' + ",".join(numbers)
		elif words:
			print ",".join(words)
		else:
			print ",".join(numbers)

