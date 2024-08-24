#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input().strip())
arr = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    print(arr[i],end=" ")
