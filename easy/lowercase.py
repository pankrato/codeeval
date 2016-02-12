#!/usr/bin/python

#https://www.codeeval.com/open_challenges/20/

import sys

f = open(sys.argv[1], 'r')

for s in f:
    print s.lower()

f.close()

