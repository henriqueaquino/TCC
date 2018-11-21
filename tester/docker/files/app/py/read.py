#!/usr/bin/env python

print "Content-type: text/html \r\n"

with open('bin', 'r') as f:
    print f.read()
f.close()
