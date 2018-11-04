#!/usr/bin/env python

import get_array3

print "Content-type: text/html \r\n"

array = get_array3.array

def mergeSort(array):
    if len(array) > 1:
        middle = int(len(array)/2)

        leftArray = array[:middle]
        rightArray = array[middle:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = 0
        j = 0
        k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            array[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            array[k] = rightArray[j]
            j += 1
            k += 1

mergeSort(array)
