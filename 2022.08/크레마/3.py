#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#
from collections import deque


def maxLength(a, k):
    # Write your code here
    result = 0
    d = deque()
    sum = 0

    for item in a:
        if sum + item <= k:
            d.append(item)
            sum += item
        else:
            while sum + item > k:
                sum -= d.popleft()
            d.append(item)
            sum += item

        result = max(result, len(d))

    return result


if __name__ == '__main__':

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    k = int(input().strip())

    result = maxLength(a, k)

    print(result)
