import copy
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = arr[:]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))