#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
f.seek(0, 2)
print f.tell()
f.close()
