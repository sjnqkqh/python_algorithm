#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'slotWheels' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY history as parameter.
#

def slotWheels(history):
    result = 0
    # Write your code here
    while len(history[0]) > 0:  # 열의 갯수만큼 반복
        max_stop_number = -1

        for i in range(len(history)):
            item = history[i]
            item = sorted(list(map(int, item)))  # 해당 행 정렬
            max_stop_number = max(max_stop_number, item[-1])  # 케이스 별 가장 큰 수 선별
            history[i] = item[:-1]  # 행에서 가장 큰 수를 제거하고 반복

        result += max_stop_number

    return result


if __name__ == '__main__':
    history_count = int(input().strip())

    history = []

    for _ in range(history_count):
        history_item = input()
        history.append(history_item)

    result = slotWheels(history)

    print(result)
