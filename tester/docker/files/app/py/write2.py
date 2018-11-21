#!/usr/bin/env python

print "Content-type: text/html \r\n"

with open('bin', 'wb') as f:
    f.seek(1048576 * 2 - 2)
    f.write(b"\0")
f.close()
