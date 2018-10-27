#!/usr/bin/env python

print 'Content-type: text/html \r\n'

import random

def test(n):
	if n % 2 == 0:
		print 'EVEN'
	else:
		print 'ODD'

test(random.randint(0, 1024))
