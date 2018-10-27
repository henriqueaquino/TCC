#!/usr/bin/env python

print "Content-type: text/html \r\n"

import get_array 

array = get_array.array

for k in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] > array[j+1]:
            aux = array[j+1]
            array[j+1] = array[j]
            array[j] = aux
