#!/usr/bin/env python

import get_array3

print "Content-type: text/html \r\n"

array = get_array3.array

for i in range(len(array)):
    indiceMenor = i
    for j in range(i + 1, len(array)):
        if (array[j] < array[indiceMenor]):
            indiceMenor = j
    aux = array[i]
    array[i] = array[indiceMenor]
    array[indiceMenor] = aux
