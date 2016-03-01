#!/usr/bin/python

#https://www.codeeval.com/open_challenges/122/

import sys
import re
import string

table = string.maketrans('abcdefghij', '0123456789')

with open(sys.argv[1], 'r') as f:

	for line in f:
		m = re.findall('[0123456789abcdefghij]', line)
		if m:
			print ''.join(m).translate(table)
		else:
			print 'NONE'
