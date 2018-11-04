#!/usr/bin/env python

print "Content-type: text/html \r\n"

with open('bin', 'wb') as f:
    f.seek(1048576 - 1)
    f.write(b"\0")
    #f.write("Hello World\n")
f.close()
