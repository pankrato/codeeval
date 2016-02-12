#!/usr/bin/python

"""Calculate Distance
https://www.codeeval.com/open_challenges/99/"""

import sys
import math
import re

def Distance(ax,ay,bx,by):
	return math.sqrt(((ax - bx)**2) + ((ay - by)**2))

f = open(sys.argv[1], 'r')

for s in f:
	m = re.findall('\d+|-\d+', s)
	print int(Distance(int(m[0]),int(m[1]),int(m[2]), int(m[3])))

f.close()

