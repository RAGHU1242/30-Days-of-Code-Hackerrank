#!/bin/python

import math
import os
import random
import re
import sys

def bubble_sort(a):
    n = len(a)
    total_swaps = 0
    
    for i in range(n):
        number_of_swaps = 0
        
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                number_of_swaps += 1
        
        total_swaps += number_of_swaps
        
        if number_of_swaps == 0:
            break
    
    print("Array is sorted in {} swaps.".format(total_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))

if __name__ == '__main__':
    n = int(raw_input().strip())  # Input for number of elements
    a = list(map(int, raw_input().rstrip().split()))  # Input for the array elements

    bubble_sort(a)
