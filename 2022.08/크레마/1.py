#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getFinalString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def getFinalString(s):
    while "AWS" in s:
        s = s.replace("AWS","")
    return s if s != '' else -1


if __name__ == '__main__':
    s = input()

    result = getFinalString(s)

    print(result)
