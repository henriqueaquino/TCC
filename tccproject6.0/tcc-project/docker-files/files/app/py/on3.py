#!/usr/bin/env python

import get_array3 

print "Content-type: text/html \r\n"

array = get_array3.array
biggest = -1

for j in range(len(array)):
    if array[j] > biggest:
        biggest = array[j]
