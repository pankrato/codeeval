#!/usr/bin/python

#https://www.codeeval.com/open_challenges/104/

import sys

dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

with open(sys.argv[1], 'r') as f:

	for line in f:
		res = ''
		num = line.strip().split(';')
		for i in range(len(num)):
			res += dic[num[i]]
		print res
