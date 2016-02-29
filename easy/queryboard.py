#!/usr/bin/python

#https://www.codeeval.com/open_challenges/87/

import sys

size = 256

matrix = [[0 for i in range(size)] for j in range(size)]

def SetCol(col, val):
	for i in range(size):
		matrix[col][i] = val

def SetRow(row, val):
	for i in range(size):
		matrix[i][row] = val

def QueryCol(col):
	print sum(matrix[col])

def QueryRow(row):
	res = 0
	for i in range(size):
		res += matrix[i][row]
	print res

with open(sys.argv[1], 'r') as f:

	for line in f:
		l = (line.strip().split())
		if l[0] == 'SetCol':
			SetCol(int(l[1]), int(l[2]))
		elif l[0] == 'SetRow':
			SetRow(int(l[1]), int(l[2]))
		elif l[0] == 'QueryCol':
			QueryCol(int(l[1]))
		elif l[0] == 'QueryRow':
			QueryRow(int(l[1]))

