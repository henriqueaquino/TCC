#!/usr/bin/env python

print "Content-type: text/html \r\n"

import random

array = []

for i in range(100):
    array.append(random.randint(0, 1024))

print "<p>"
print array
print "</p>"

biggest = -1
for j in range(100):
    if array[j] > biggest:
        biggest = array[j]

print "<p>"
print biggest
print "</p>"
