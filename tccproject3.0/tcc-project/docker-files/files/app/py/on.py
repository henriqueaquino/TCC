#!/usr/bin/env python

import get_array 

print "Content-type: text/html \r\n"

array = get_array.array
biggest = -1

for j in range(len(array)):
    if array[j] > biggest:
        biggest = array[j]
