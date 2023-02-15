import heapq
import sys

N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr, int(sys.stdin.readline()))

while arr:
    print(heapq.heappop(arr))
