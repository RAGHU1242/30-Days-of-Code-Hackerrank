#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    b=bin(n)[2:]
    arr1=b.split('0')
    max1=max(len(i) for i in arr1)
    print(max1)
