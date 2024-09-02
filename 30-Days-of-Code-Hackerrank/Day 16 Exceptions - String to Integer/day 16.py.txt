#!/bin/python3

import math
import os
import random
import re
import sys

s = input().strip()  
try:
    number = int(s)
    print(number)
except ValueError:
    print("Bad String")
