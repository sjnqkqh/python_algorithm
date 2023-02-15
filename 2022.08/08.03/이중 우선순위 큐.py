import heapq
import sys
from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []

    for _ in range(N):
        line = list(sys.stdin.readline().split())
        do, num = line[0], int(line[1])

        if do == "I":
            heapq.heappush(arr, num)
        else:
            if arr:
                if num == 1:
                    arr.pop()
                else:
                    arr = arr[1:]

    if len(arr) == 0:
        print("EMPTY")
    else:
        print(arr[-1], arr[0], sep=" ")
