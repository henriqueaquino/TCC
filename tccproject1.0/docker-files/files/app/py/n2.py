#!/usr/bin/env python

print "Content-type: text/html \r\n"

import random

array = []

for i in range(100):
    array.append(random.randint(0, 1024))

print "<p>"
print array
print "</p>"

for k in range(100):
    for j in range(99):
        if array[j] > array[j+1]:
            aux = array[j+1]
            array[j+1] = array[j]
            array[j] = aux

print "<p>"
print array
print "</p>"
