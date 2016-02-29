#!/usr/bin/python

#https://www.codeeval.com/open_challenges/22/

import sys

def Fibonacci(n):
	return n if n < 2 else Fibonacci(n-1) + Fibonacci(n-2)

with open(sys.argv[1], 'r') as f:
	for line in f:
		print Fibonacci(int(line.strip()))

