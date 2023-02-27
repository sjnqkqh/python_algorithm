import bisect
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
dp = []

for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))
