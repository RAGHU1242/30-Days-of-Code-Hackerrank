#!binpython

import math
import os
import random
import re
import sys



if __name__ == '__main__'
    arr = [list(map(int, raw_input().rstrip().split())) for _ in xrange(6)]
    maxSum = -100
    for i in range(4)
        for j in range(4)
            theSum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                      arr[i+1][j+1] +
                      arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            maxSum = max(maxSum, theSum)

    print(maxSum)
