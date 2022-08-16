#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findRange' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER num as parameter.
#

def findRange(num):
    # Write your code here
    num_list = list(str(num))
    number_to_max = 0
    number_to_min = 0

    for i in range(len(num_list)):
        if num_list[i] != '9':
            number_to_max = num_list[i]
            break

    max_number = 0
    for i in range(len(num_list)):
        if num_list[i] == number_to_max:
            max_number = (max_number * 10) + 9
        else:
            max_number = (max_number * 10) + int(num_list[i])

    min_number = 0
    is_first = False
    for i in range(len(num_list)):
        if i == 0 and num_list[i] != '1':
            number_to_min = num_list[i]
            is_first = True
            break

        if i > 0 and num_list[i] != '0' and num_list[i] != num_list[0]:
            number_to_min = num_list[i]
            break

    if is_first:
        for i in range(len(num_list)):
            if num_list[i] == number_to_min:
                min_number = (min_number * 10) + 1
            else:
                min_number = (min_number * 10) + int(num_list[i])
    else:
        for i in range(len(num_list)):
            if num_list[i] == number_to_min:
                min_number = (min_number * 10)
            else:
                min_number = (min_number * 10) + int(num_list[i])

    return max_number- min_number


if __name__ == '__main__':
    num = int(input().strip())

    result = findRange(num)

    print(result)
