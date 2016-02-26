#!/usr/bin/python

#https://www.codeeval.com/open_challenges/192/

import sys
import math
import re

RoseOfWind = {0:'here', 10:'N', -10:'S', 1:'E', -1:'W',
	11:'NE', 9:'NW', -11:'SW', -9:'SE'}

def Direction(ax, ay, bx, by):
	EorW = math.copysign(1, bx - ax) if bx - ax else 0
	NorS = math.copysign(10, by - ay) if by - ay else 0
	return RoseOfWind[EorW + NorS]

with open(sys.argv[1], 'r') as f:

	for s in f:
		m = re.findall('\d+|-\d+', s)
		print Direction(int(m[0]),int(m[1]),int(m[2]), int(m[3]))

