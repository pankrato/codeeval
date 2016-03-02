#!/usr/bin/python

#https://www.codeeval.com/open_challenges/113/

import sys

with open(sys.argv[1], 'r') as f:

	for line in f:
		inp = line.strip().split('|')
		list1 = [int(x) for x in (inp[0].strip().split())]
		list2 = [int(x) for x in (inp[1].strip().split())]
		result = [str(list1[i] * list2[i]) for i in range(len(list1))]
		print ' '.join(result)
